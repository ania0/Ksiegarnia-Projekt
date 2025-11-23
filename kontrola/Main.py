from encje.FabrykaKsiazek import FabrykaKsiazek
from kontrola.KsiegarniaKontrolaFacade import KsiegarniaKontrolaFacade
from encje.FasadaEncji import FasadaEncji
from encje.UzytkownikDAO import UzytkownikDAO
from encje.KsiazkaDAO import KsiazkaDAO
from encje.ZamowienieDAO import ZamowienieDAO



def main():


    print("--- START SYSTEMU (Tryb tekstowy 'Main.py') ---")

    print("\n[Krok 1] Przygotowanie danych testowych...")
    dane_rejestracji = {"login": "anna", "haslo": "pass123"}
    dane_logowania_klient = {"login": "anna", "haslo": "pass123"}
    dane_logowania_admin = {"login": "admin", "haslo": "admin123"}
    pusty_koszyk = {"id_ksiazek": [1, 3]}

    print("\n[Krok 2] Budowanie architektury...")

    uzytkownik_dao = UzytkownikDAO()
    ksiazka_dao = KsiazkaDAO()
    zamowienie_dao = ZamowienieDAO()
    fabryka_ksiazek = FabrykaKsiazek()

    encje_fasada = FasadaEncji(
        repoUzytkownika=uzytkownik_dao,
        repoKsiazek=ksiazka_dao,
        repoZamowien=zamowienie_dao,
        fabrykaKsiazek=fabryka_ksiazek
    )

    fasada_kontroli = KsiegarniaKontrolaFacade(encje_fasada=encje_fasada)

    print("\n--- System gotowy. Rozpoczynam testy... ---")

    def testuj_przypadek_uzycia(nazwa_pu, funkcja_do_wywolania):
        print(f"\n--- Testowanie {nazwa_pu} ---")
        try:
            wynik = funkcja_do_wywolania()
            print(f"Wynik testu: {wynik}")
        except NotImplementedError as e:
            print(f">>> OK: Poprawnie przechwycono błąd STUB: {e}")
        except Exception as e:
            print(f"XXX BŁĄD KRYTYCZNY: {e}")

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

    print("\n--- ZAKOŃCZONO TESTY 'Main.py' ---")



if __name__ == "__main__":
    main()