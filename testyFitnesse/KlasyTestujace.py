import sys
import os

# --- KONFIGURACJA ŚCIEŻEK ---
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from SetUp import SetUp
from encje.FabrykaKsiazek import FabrykaKsiazek
from encje.Klient import Klient
from encje.Zamowienie import Zamowienie
from encje.PozycjaZamowienia import PozycjaZamowienia


class KlasyTestujace:
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        print("--- INICJALIZACJA SYSTEMU TESTOWEGO ---")

    # --- METODY POMOCNICZE (KONWERSJA DANYCH) ---
    def _safe_float(self, val):
        try:
            return float(str(val).replace(',', '.'))
        except:
            return 0.0

    def _napraw_isbn(self, isbn):
        try:
            s = str(isbn).replace("-", "").strip()
            if len(s) < 13: s = s.ljust(13, '0')[:13]
            return int(s)
        except:
            return 9999999999999

    # ==========================================
    # UŻYTKOWNICY
    # ==========================================

    def stworz_konto(self, imie, nazwisko, email, haslo, adres):
        print(f"[AKCJA] Tworzenie konta: {email}")
        try:
            # Uzywamy nazwy pola 'hashHasla' zgodnie z Twoja klasa Klient
            klient = Klient(imie, nazwisko, email, hashHasla=haslo, adresWysylki=adres, klientLojalny=False)
            SetUp.Inwentarz.rejestrujUzytkownika(klient)
            print(f"[SUKCES] Utworzono uzytkownika ID: {klient.id if hasattr(klient, 'id') else '?'}")
            return "True"
        except Exception as e:
            print(f"[BLAD] {e}")
            return "False"

    def sprawdz_logowanie(self, email, haslo):
        print(f"[AKCJA] Logowanie: {email} wpisujac haslo: {haslo}")
        u = SetUp.Inwentarz.znajdzUzytkownikaPoEmailu(email)

        if not u:
            print("[PORAZKA] Nie znaleziono uzytkownika o takim emailu.")
            return "False"

        # Teraz odwolywanie sie do pola zgodnie z Twoim kodem: hashHasla
        print(f"[INFO] Znaleziono uzytkownika: {u.imie} {u.nazwisko}, Haslo w bazie: {u.hashHasla}")

        if str(u.hashHasla) == str(haslo):
            print("[SUKCES] Haslo poprawne.")
            return "True"

        print(f"[PORAZKA] Haslo niepoprawne.")
        return "False"

    def usun_uzytkownika(self, email):
        print(f"[AKCJA] Usuwanie uzytkownika: {email}")
        try:
            u = SetUp.Inwentarz.znajdzUzytkownikaPoEmailu(email)
            if u:
                SetUp.Inwentarz.usun(u.id)
                print("[SUKCES] Uzytkownik usuniety.")
                return "True"
            print("[INFO] Nie bylo kogo usuwac.")
            return "False"
        except Exception as e:
            print(f"[BLAD] {e}")
            return "False"

    # ==========================================
    # KATALOG KSIAZEK
    # ==========================================

    def dodaj_ksiazke(self, tytul, cena, isbn):
        print(f"[AKCJA] Dodawanie ksiazki: '{tytul}', Cena: {cena}, ISBN: {isbn}")
        try:
            # Fabryka tworzy ksiazke
            k = FabrykaKsiazek().utworzKsiazke(
                typ="papierowa",
                tytul=tytul,
                autor="AutorTestowy",
                cena=self._safe_float(cena),
                ISBN=self._napraw_isbn(isbn),
                gatunek="GatunekTestowy",
                stanMagazynowy=10,
                opis="Opis testowy"
            )
            SetUp.Inwentarz.dodajKsiazke(k)
            print("[SUKCES] Ksiazka dodana do repozytorium.")
            return "True"
        except Exception as e:
            print(f"[BLAD] {e}")
            return "False"

    def czy_ksiazka_istnieje(self, tytul):
        print(f"[AKCJA] Wyszukiwanie w katalogu ksiazki: '{tytul}'")

        # Uzywamy metody Fasady: pobierzWszystkie() zamiast szukac pola .ksiazki
        wszystkie = SetUp.Inwentarz.pobierzWszystkie()

        for k in wszystkie:
            if k.tytul == tytul:
                print(f"[SUKCES] Znaleziono ksiazke ID: {k.id}")
                return "True"

        print("[INFO] Ksiazki nie znaleziono.")
        return "False"

    def edytuj_cene_ksiazki(self, isbn, nowa_cena):
        print(f"[AKCJA] Zmiana ceny dla ISBN: {isbn} na {nowa_cena}")
        isbn_val = self._napraw_isbn(isbn)

        k = SetUp.Inwentarz.pobierzPoISBN(isbn_val)
        if k:
            # Uzywamy metody Fasady: aktualizujDane
            wynik = SetUp.Inwentarz.aktualizujDane(
                ksiazka=k,
                nowyTytul=None, nowyAutor=None, nowyGatunek=None, nowyOpis=None,
                nowaCena=self._safe_float(nowa_cena)
            )
            if wynik is None:  # None oznacza sukces w Twojej Fasadzie
                print("[SUKCES] Cena zaktualizowana.")
                return "True"
            else:
                print(f"[BLAD] Fasada zwrocila blad: {wynik}")
                return "False"

        print("[BLAD] Nie znaleziono ksiazki do edycji.")
        return "False"

    def pobierz_cene_ksiazki(self, isbn):
        k = SetUp.Inwentarz.pobierzPoISBN(self._napraw_isbn(isbn))
        if k:
            return str(k.cena)
        return "0.0"

    def usun_ksiazke(self, isbn):
        print(f"[AKCJA] Usuwanie ksiazki ISBN: {isbn}")
        isbn_val = self._napraw_isbn(isbn)
        try:
            SetUp.Inwentarz.usunKsiazke(isbn_val)
            print("[SUKCES] Polecenie usuniecia wykonane.")
            return "True"
        except Exception as e:
            print(f"[BLAD] {e}")
            return "False"

    def zmien_stan(self, isbn, ilosc):
        print(f"[AKCJA] Ustawianie stanu magazynowego ISBN {isbn} na {ilosc}")
        try:
            SetUp.Inwentarz.aktualizujStan(self._napraw_isbn(isbn), int(ilosc))
            return "True"
        except Exception as e:
            print(f"[BLAD] {e}")
            return "False"

    def pobierz_stan(self, isbn):
        k = SetUp.Inwentarz.pobierzPoISBN(self._napraw_isbn(isbn))
        if k:
            return k.stanMagazynowy
        return -1

    # ==========================================
    # ZAMOWIENIA
    # ==========================================

    def zloz_zamowienie(self, email_klienta, isbn, ilosc, tryb_gosc="False"):
        try:
            print(f"[AKCJA] Skladanie zamowienia. Klient: {email_klienta}, ISBN: {isbn}, Ilosc: {ilosc}")
            isbn_val = self._napraw_isbn(isbn)
            ilosc_int = int(ilosc)

            # 1. Identyfikacja Klienta
            if tryb_gosc == "True":
                print("[INFO] Tryb GOSC - tworzenie tymczasowego klienta.")
                klient = Klient("Gosc", "Gosc", email_klienta, "brak", "Adres Goscia", False)
            else:
                klient = SetUp.Inwentarz.znajdzUzytkownikaPoEmailu(email_klienta)
                if not klient:
                    print("[BLAD] Nie znaleziono klienta w bazie.")
                    return "Error: Brak uzytkownika"

            # 2. Weryfikacja Ksiazki
            ksiazka = SetUp.Inwentarz.pobierzPoISBN(isbn_val)
            if not ksiazka:
                print("[BLAD] Nie znaleziono ksiazki.")
                return "Error: Brak ksiazki"

            # 3. Sprawdzenie stanu magazynowego
            if ksiazka.stanMagazynowy < ilosc_int:
                print(f"[BLAD] Za malo towaru. Jest: {ksiazka.stanMagazynowy}, Chcesz: {ilosc_int}")
                return "Error: Za malo towaru"

            # 4. Proces Zamowienia (Symulacja Kontrolera)
            zamowienie = Zamowienie()
            pozycja = PozycjaZamowienia(ksiazka, ilosc_int, ksiazka.cena)
            zamowienie.dodajPozycje(pozycja)

            # Obliczenie ceny z uwzglednieniem rabatow (Fasada)
            cena_total = SetUp.Inwentarz.obliczCeneOstateczna(zamowienie, klient)
            print(f"[INFO] Cena ostateczna po rabatach: {cena_total}")

            # Zapis zamowienia
            SetUp.Inwentarz.zapiszZamowienie(zamowienie)

            # Aktualizacja stanu magazynowego
            nowy_stan = ksiazka.stanMagazynowy - ilosc_int
            SetUp.Inwentarz.aktualizujStan(isbn_val, nowy_stan)

            print("[SUKCES] Zamowienie zlozone i zapisane.")
            return "True"

        except Exception as e:
            print(f"[CRITICAL ERROR] {e}")
            return f"Error: {e}"