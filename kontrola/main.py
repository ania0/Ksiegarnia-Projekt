# Importy z obu pakietów
from kontrola.ksiegarnia_kontrola_facade import KsięgarniaKontrolaFacade
from encje.fasada_encji import FasadaEncji
from encje.uzytkownik_dao import UzytkownikDAO
from encje.ksiazka_dao import KsiazkaDAO
from encje.zamowienie_dao import ZamowienieDAO
from encje.fabryka_zamowienia import FabrykaZamowienia


def main():
    """
    Główna funkcja uruchomieniowa, realizująca
    "Ideę testowego działania" w trybie tekstowym.
    """

    print("--- START SYSTEMU (Tryb tekstowy 'main.py') ---")

    # 1) Przygotowanie danych testowych
    print("\n[Krok 1] Przygotowanie danych testowych...")
    dane_rejestracji = {"login": "anna", "haslo": "pass123"}
    dane_logowania_klient = {"login": "anna", "haslo": "pass123"}
    dane_logowania_admin = {"login": "admin", "haslo": "admin123"}
    pusty_koszyk = {"id_ksiazek": [1, 3]}

    # 2) Przygotowanie klas i obiektów (Dependency Injection)
    print("\n[Krok 2] Budowanie architektury...")

    # (Od dołu) Tworzymy implementacje DAO (Stuby)
    uzytkownik_dao = UzytkownikDAO()
    ksiazka_dao = KsiazkaDAO()
    zamowienie_dao = ZamowienieDAO()
    fabryka_zamowien = FabrykaZamowienia()

    # Tworzymy Fasadę Encji i wstrzykujemy jej zależności
    fasada_encji = FasadaEncji(
        repo_uzytkownika=uzytkownik_dao,
        repo_ksiazek=ksiazka_dao,
        repo_zamowien=zamowienie_dao,
        fabryka_zamowien=fabryka_zamowien
    )

    # Tworzymy Fasadę Kontroli (główny punkt wejścia)
    fasada_kontroli = KsięgarniaKontrolaFacade(fasada_encji=fasada_encji)

    print("\n--- System gotowy. Rozpoczynam testy... ---")

    # 3), 4), 5) Testowanie przypadków użycia

    # Funkcja pomocnicza do testowania
    def testuj_przypadek_uzycia(nazwa_pu, funkcja_do_wywolania):
        print(f"\n--- Testowanie {nazwa_pu} ---")
        try:
            wynik = funkcja_do_wywolania()
            print(f"Wynik testu: {wynik}")
        except NotImplementedError as e:
            print(f">>> OK: Poprawnie przechwycono błąd STUB: {e}")
        except Exception as e:
            print(f"XXX BŁĄD KRYTYCZNY: {e}")

    # Uruchomienie wszystkich testów
    testuj_przypadek_uzycia("PU01: Stworzenie konta",
                            lambda: fasada_kontroli.stworzKonto(dane_rejestracji))

    testuj_przypadek_uzycia("PU02: Logowanie klienta",
                            lambda: fasada_kontroli.zalogujKlienta(dane_logowania_klient["login"],
                                                                   dane_logowania_klient["haslo"]))

    testuj_przypadek_uzycia("PU14: Logowanie administratora",
                            lambda: fasada_kontroli.zalogujAdministratora(dane_logowania_admin["login"],
                                                                          dane_logowania_admin["haslo"]))

    testuj_przypadek_uzycia("PU07: Złożenie zamówienia",
                            lambda: fasada_kontroli.zlozZamowienie(pusty_koszyk))

    testuj_przypadek_uzycia("PU03: Usunięcie konta",
                            lambda: fasada_kontroli.usunKonto())

    testuj_przypadek_uzycia("PU13: Przeglądanie raportu",
                            lambda: fasada_kontroli.przegladajRaporty())

    testuj_przypadek_uzycia("PU04: Przeglądanie książek",
                            lambda: fasada_kontroli.przegladajKsiazki())

    testuj_przypadek_uzycia("PU06: Przeglądanie historii",
                            lambda: fasada_kontroli.przegladajHistorie())

    print("\n--- ZAKOŃCZONO TESTY 'main.py' ---")


# Standardowe uruchomienie pliku main.py
if __name__ == "__main__":
    main()