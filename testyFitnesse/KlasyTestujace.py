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
        pass

    # --- METODY POMOCNICZE ---
    def _safe_int(self, value, default=0):
        try:
            s = str(value).strip().lower()
            if s in ['true', 'false']: return default
            return int(float(s))
        except:
            return default

    def _safe_float(self, value, default=0.0):
        try:
            s = str(value).strip().lower()
            if s in ['true', 'false']: return default
            return float(s.replace(',', '.'))
        except:
            return default

    def _napraw_isbn(self, isbn):
        try:
            czysty = str(isbn).replace("-", "").replace(" ", "").strip()
            if czysty.lower() in ['true', 'false']: return 9999999999999
            if len(czysty) < 13: czysty = czysty.ljust(13, '0')[:13]
            return int(czysty)
        except:
            return 9999999999999

    # --- ASERCJE STANU ---
    def stan_uzytkownikow(self):
        return SetUp.Inwentarz.ileUzytkownikow()

    def stan_ksiazek(self):
        return SetUp.Inwentarz.ileKsiazek()

    # --- PU01: Rejestracja ---
    def stworz_konto(self, imie, nazwisko, email, haslo, adres):
        stan_przed = self.stan_uzytkownikow()
        try:
            klient = Klient(imie, nazwisko, email, haslo, adres, klientLojalny=False)
            SetUp.Inwentarz.rejestrujUzytkownika(klient)
        except Exception as e:
            return f"False: {e}"
        stan_po = self.stan_uzytkownikow()
        return "True" if stan_po > stan_przed else "False"

    # --- PU03: Usuwanie ---
    def usun_uzytkownika(self, email):
        try:
            uzytkownik = SetUp.Inwentarz.znajdzUzytkownikaPoEmailu(email)
            if uzytkownik:
                SetUp.Inwentarz.usun(uzytkownik.id)
                return "True"
            return "False"
        except Exception:
            return "False"

    # --- PU09: Dodawanie książki ---
    def dodaj_ksiazke(self, typ, tytul, autor, cena, isbn, gatunek):
        stan_przed = self.stan_ksiazek()
        try:
            ksiazka = FabrykaKsiazek().utworzKsiazke(
                typ="papierowa", tytul=tytul, autor=autor,
                cena=self._safe_float(cena), ISBN=self._napraw_isbn(isbn),
                gatunek=gatunek, stanMagazynowy=10, opis="Test"
            )
            SetUp.Inwentarz.dodajKsiazke(ksiazka)
        except Exception:
            return "False"
        return "True" if self.stan_ksiazek() > stan_przed else "False"

    # --- PU11: Zmiana Stanu ---
    def zmien_stan(self, isbn, nowa_ilosc):
        """
        Zwraca LICZBĘ (int) nowej ilości, aby Robot mógł sprawdzić:
        Should Be Equal As Integers    ${stan}    50
        """
        try:
            ilosc_int = self._safe_int(nowa_ilosc, default=-1)
            isbn_val = self._napraw_isbn(isbn)

            if ilosc_int == -1: return 0

            SetUp.Inwentarz.aktualizujStan(isbn_val, ilosc_int)

            # Weryfikujemy i ZWRACAMY LICZBĘ
            ksiazka = SetUp.Inwentarz.pobierzPoISBN(isbn_val)
            if ksiazka:
                return ksiazka.stanMagazynowy
            return 0
        except Exception:
            return 0

    # --- PU RABAT ---
    def oblicz_cene_dla_klienta(self, czy_lojalny, cena_bazowa):
        """
        Argumenty dopasowane do pliku .robot:
        1. czy_lojalny (True/False)
        2. cena_bazowa (kwota)
        """
        try:
            cena_val = self._safe_float(cena_bazowa)
            jest_lojalny = str(czy_lojalny).lower() in ['true', 'yes', '1']

            # 1. Klient
            klient = Klient("Test", "K", "t@t.pl", "pass", "Adr", klientLojalny=jest_lojalny)

            # 2. Zamówienie
            ksiazka = FabrykaKsiazek().utworzKsiazke(
                "papierowa", "T", "A", cena_val, 9789999999999, "G", 5, "O"
            )
            zamowienie = Zamowienie()
            zamowienie.dodajPozycje(PozycjaZamowienia(ksiazka, 1, cena_val))

            # 3. Obliczenie przez Fasade
            wynik = SetUp.Inwentarz.obliczCeneOstateczna(zamowienie, klient)

            return str(wynik)  # Zwracamy jako string, bo Robot porównuje "90.0"

        except Exception as e:
            return f"Error: {e}"