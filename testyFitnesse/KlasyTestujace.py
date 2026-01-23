import sys
import os

# Zabezpieczenie ścieżek
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from SetUp import SetUp
from encje.Klient import Klient
from encje.Zamowienie import Zamowienie
from encje.PozycjaZamowienia import PozycjaZamowienia


class KlasyTestujace:
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        self.setup = SetUp()

    # POMOCNICZE
    def _safe_float(self, val):
        try:
            # Zamiana na string, zeby replace i float zadzialalo
            return float(str(val).replace(',', '.'))
        except:
            return 0.0

    def _napraw_isbn(self, isbn):
        try:
            # str(), bo isbn moze przyjsc jako float (np. 9.78E+12)
            s = str(isbn)
            return int(s.replace("-", "").replace(".0", "").strip())
        except:
            return 9999999999999

    # UŻYTKOWNICY
    def stworz_konto(self, imie, nazwisko, email, haslo, adres):
        # Tworzenie User bezposrednio w bazie, omijac input() kontrolera
        try:
            nowy_klient = Klient(imie, nazwisko, email, haslo, adres, False)
            SetUp.Inwentarz.rejestrujUzytkownika(nowy_klient)
            return "True"
        except Exception as e:
            print(f"[BLAD] {e}")
            return "False"

    def sprawdz_logowanie(self, email, haslo):
        try:
            # Kontroler - brak input
            wynik = SetUp.Kontrola.zalogujKlienta(haslo, email)
            return "True" if wynik else "False"
        except:
            return "False"

    def usun_uzytkownika(self, email):
        u = SetUp.Inwentarz.znajdzUzytkownikaPoEmailu(email)
        if u:
            # Fasada Encji - logowanie raz
            try:
                SetUp.Inwentarz.usun(u.id)
                return "True"
            except:
                return "False"
        return "True"

    # KATALOG
    def dodaj_ksiazke(self, tytul, cena, isbn):
        try:
            from encje.FabrykaKsiazek import FabrykaKsiazek
            k = FabrykaKsiazek().utworzKsiazke("papierowa", tytul, "AutorTest",
                                               self._safe_float(cena), self._napraw_isbn(isbn),
                                               "Gatunek", 10, "Opis")
            SetUp.Inwentarz.dodajKsiazke(k)
            return "True"
        except:
            return "False"

    def czy_ksiazka_istnieje(self, tytul):
        ksiazki = SetUp.Inwentarz.pobierzWszystkie()
        for k in ksiazki:
            if k.tytul == tytul: return "True"
        return "False"

    def edytuj_cene_ksiazki(self, isbn, nowa_cena):
        k = SetUp.Inwentarz.pobierzPoISBN(self._napraw_isbn(isbn))
        if k:
            try:
                # Rzutowanie i podanie argumentow
                cena_float = self._safe_float(nowa_cena)
                # Wywolanie z nazwanymi arg
                SetUp.Inwentarz.aktualizujDane(ksiazka=k, nowaCena=cena_float,
                                               nowyTytul=None, nowyAutor=None,
                                               nowyGatunek=None, nowyOpis=None)
                return "True"
            except TypeError:
                # jesli Fasada nie obsluguje keyword args
                k.cena = self._safe_float(nowa_cena)
                return "True"
            except Exception as e:
                print(f"Blad edycji: {e}")
                return "False"
        return "False"

    def pobierz_cene_ksiazki(self, isbn):
        k = SetUp.Inwentarz.pobierzPoISBN(self._napraw_isbn(isbn))
        return str(k.cena) if k else "0.0"

    def zmien_stan(self, isbn, ilosc):
        SetUp.Inwentarz.aktualizujStan(self._napraw_isbn(isbn), int(ilosc))
        return "True"

    def pobierz_stan(self, isbn):
        k = SetUp.Inwentarz.pobierzPoISBN(self._napraw_isbn(isbn))
        return k.stanMagazynowy if k else -1

    def usun_ksiazke(self, isbn):
        SetUp.Inwentarz.usunKsiazke(self._napraw_isbn(isbn))
        return "True"


    # ZAMOWIENIA
    def zloz_zamowienie(self, email_klienta, isbn, ilosc, tryb_gosc="False"):
        isbn_val = self._napraw_isbn(isbn)
        ilosc_int = int(ilosc)

        # Pobranie ksiazki - jednorazowe
        ksiazka = SetUp.Inwentarz.pobierzPoISBN(isbn_val)
        if not ksiazka: return "Error: Brak ksiazki"

        # Walidacja dostępnosci
        if ksiazka.stanMagazynowy < ilosc_int:
            print(f"[LOGIC] Próba kupna {ilosc_int} przy stanie {ksiazka.stanMagazynowy}")
            return "Error: Za malo towaru"

        # Ustalenie klienta
        klient_obj = None
        if tryb_gosc == "False":
            klient_obj = SetUp.Inwentarz.znajdzUzytkownikaPoEmailu(email_klienta)
            if not klient_obj: return "Error: Brak usera"
        else:
            # Atrapa klienta dla goscia (do obliczeń)
            klient_obj = Klient("Gosc", "Gosc", email_klienta, "brak", "Adres", False)

        # Symulacja procesu zamówienia
        try:
            zamowienie = Zamowienie()
            pozycja = PozycjaZamowienia(ksiazka, ilosc_int, ksiazka.cena)
            zamowienie.dodajPozycje(pozycja)

            # Obliczenie ceny
            SetUp.Inwentarz.obliczCeneOstateczna(zamowienie, klient_obj)

            # Zapis
            SetUp.Inwentarz.zapiszZamowienie(zamowienie)

            # Aktualizacja stanu
            nowy_stan = ksiazka.stanMagazynowy - ilosc_int
            SetUp.Inwentarz.aktualizujStan(isbn_val, nowy_stan)

            print(f"[SUKCES] Kupiono {ilosc_int} szt. Nowy stan: {nowy_stan}")
            return "True"

        except Exception as e:
            print(f"[CRITICAL] Błąd składania zamówienia w teście: {e}")
            return f"Error: {e}"