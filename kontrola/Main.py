from encje.Administrator import Administrator
from encje.DekoratorRabatuLojalnosciowego import DekoratorRabatuLojalnosciowego
from encje.FabrykaKsiazek import FabrykaKsiazek
from kontrola.KsiegarniaKontrolaFacade import KsiegarniaKontrolaFacade
from encje.FasadaEncji import FasadaEncji
from encje.UzytkownikDAO import UzytkownikDAO
from encje.KsiazkaDAO import KsiazkaDAO
from encje.ZamowienieDAO import ZamowienieDAO
from encje.Klient import Klient

#głównie trzeba będzie zaimplementować w jakiś sposób zarządzanie katalogiem, bo teraz to w ogóle nie jest testowane

def main():
    print("START")

    print("\nPrzygotowanie danych testowych")
    # Dane testowe
    haslo_test = "haslo123"
    email_test = "anna@test.pl"

    # Symulacja koszyka (lista ID)
    koszyk_ISBN_ksiazek = [1, 3]
    id_klienta_test = 1

    print("\nBudowanie architektury")

    uzytkownik_dao = UzytkownikDAO()
    ksiazka_dao = KsiazkaDAO()
    zamowienie_dao = ZamowienieDAO()
    fabryka_ksiazek = FabrykaKsiazek()
    dekorator_rabatu = DekoratorRabatuLojalnosciowego

    encje_fasada = FasadaEncji(
        repoKsiazek=ksiazka_dao,
        repoUzytkownika=uzytkownik_dao,
        repoZamowien=zamowienie_dao,
        fabrykaKsiazek=fabryka_ksiazek,
        dekoratorRabatu=dekorator_rabatu
    )
    admin_uzytkownik = Administrator(
        imie="Admin",
        nazwisko="Admin",
        email="admin@test.pl",
        hashHasla="admin123",
        id = 1
    )
    encje_fasada.rejestrujUzytkownika(admin_uzytkownik)
    print("Zarejestrowano administratora testowego: admin@test.pl")

    # Tworzenie klienta z pełnymi danymi w main.py
    nowy_klient = Klient(
        imie="Anna",
        nazwisko="Testowa",
        email=email_test,
        hashHasla=haslo_test,
        adresWysylki="ul. Testowa 2",
        klientLojalny=False
    )
    encje_fasada.rejestrujUzytkownika(nowy_klient)
    print(f"Pomyślnie zarejestrowano nowego klienta: {email_test}")

    fasada_kontroli = KsiegarniaKontrolaFacade(encje_fasada=encje_fasada)

    print("\nRozpoczęcie testów")

    # def testuj_przypadek_uzycia(nazwa_pu, funkcja_do_wywolania):
    #     print(f"\nTestowanie {nazwa_pu}")
    #     try:
    #         wynik = funkcja_do_wywolania()
    #         print(f"Wynik testu: {wynik}")
    #     except NotImplementedError as e:
    #         print(f">>> OK: Poprawnie przechwycono błąd STUB: {e}")
    #     except Exception as e:
    #         print(f" BŁĄD KRYTYCZNY: {e}")
    #         import traceback
    #         traceback.print_exc()

    def testuj_przypadek_uzycia(nazwa_pu, funkcja_do_wywolania):
        print(f"\nTestowanie {nazwa_pu}")
        try:
            wynik = funkcja_do_wywolania()

            # 🔥✨ UNIWERSALNY PIĘKNY PRINT OBIEKTÓW ✨🔥
            if hasattr(wynik, "__dict__"):
                print(f"Wynik testu ({wynik.__class__.__name__}):")
                for pole, wartosc in wynik.__dict__.items():
                    print(f"  - {pole}: {wartosc}")
            else:
                print(f"Wynik testu: {wynik}")

        except NotImplementedError as e:
            print(f">>> OK: Poprawnie przechwycono błąd STUB: {e}")
        except Exception as e:
            print(f" BŁĄD KRYTYCZNY: {e}")
            import traceback
            traceback.print_exc()


    while True:
        print("1. PU01: Stworzenie konta")
        print("2. PU02: Logowanie klienta do systemu")
        print("3. PU14: Logowanie administratora")
        print("4. Wyjście z logowania/stworzenia konta")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            imie = input("Podaj imię: ")
            nazwisko = input("Podaj nazwisko: ")
            email = input("Podaj email: ")
            haslo = input("Podaj hasło: ")
            adres = input("Podaj adres wysyłki: ")
            klient = Klient(imie, nazwisko, email, haslo, adres, False)
            encje_fasada.rejestrujUzytkownika(klient)
            print(f"Pomyślnie zarejestrowano klienta: {imie} {nazwisko}")

        elif wybor == "2":
            email = input("Email klienta: ")
            haslo = input("Hasło klienta: ")
            klient = fasada_kontroli.zalogujKlienta(haslo, email)
            if klient:
                print(f"Zalogowano klienta: {klient.imie} {klient.nazwisko}")
            else:
                print("Nieprawidłowy login lub hasło klienta.")

        elif wybor == "3":
            email = input("Email admina: ")
            haslo = input("Hasło admina: ")
            admin = fasada_kontroli.zalogujAdministratora(haslo, email)
            if admin:
                print(f"Zalogowano administratora: {admin.imie} {admin.nazwisko}")
            else:
                print("Nieprawidłowy login lub hasło administratora.")

        elif wybor == "4":
            print("Koniec pętli logowania/stworzenia konta.")
            break

        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")

    # testuj_przypadek_uzycia("PU01: Stworzenie konta",
    #                         lambda: fasada_kontroli.stworzKonto(haslo_test, email_test))
    #
    # testuj_przypadek_uzycia("PU02: Logowanie klienta do systemu",
    #                         lambda: fasada_kontroli.zalogujKlienta(haslo_test, email_test))
    #
    # testuj_przypadek_uzycia("PU14: Logowanie administratora",
    #                         lambda: fasada_kontroli.zalogujAdministratora("admin123", "admin@test.pl"))

    testuj_przypadek_uzycia("PU04: Przeglądanie książek",
                            lambda: fasada_kontroli.przegladajKsiazki())

    testuj_przypadek_uzycia("PU06: Przeglądanie historii",
                            lambda: fasada_kontroli.przegladajHistorie(id_klienta_test))

    testuj_przypadek_uzycia("PU07: Złożenie zamówienia",
                            lambda: fasada_kontroli.zlozZamowienie(id_klienta_test, koszyk_ISBN_ksiazek))

    testuj_przypadek_uzycia("PU05: Wybranie książki",
                            lambda: fasada_kontroli.wybierzKsiazke(koszyk_ISBN_ksiazek[0]))


    testuj_przypadek_uzycia("PU08: Zarządzanie katalogiem",
                             lambda: fasada_kontroli.zarzadzajKatalogiem())
    #opcje PU09-P12

    testuj_przypadek_uzycia("PU04: Przeglądanie książek",
                            lambda: fasada_kontroli.przegladajKsiazki())

    testuj_przypadek_uzycia("PU03: Usunięcie konta",
                            lambda: fasada_kontroli.usunKonto(id_klienta_test))

    testuj_przypadek_uzycia("PU13: Przeglądanie raportów sprzedażowych",
                            lambda: fasada_kontroli.przegladajRaporty())


    print("\n ZAKOŃCZONO TESTY 'Main.py'")


if __name__ == "__main__":
    main()