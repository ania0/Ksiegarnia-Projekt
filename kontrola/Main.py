from encje.Administrator import Administrator
from encje.DekoratorRabatuLojalnosciowego import DekoratorRabatuLojalnosciowego
from encje.FabrykaKsiazek import FabrykaKsiazek
from kontrola.KsiegarniaKontrolaFacade import KsiegarniaKontrolaFacade
from encje.FasadaEncji import FasadaEncji
from encje.UzytkownikDAO import UzytkownikDAO
from encje.KsiazkaDAO import KsiazkaDAO
from encje.ZamowienieDAO import ZamowienieDAO
from encje.Klient import Klient
import random  # Dodano do generowania hasła dla gościa


def menu_goscia(fasada_kontroli: KsiegarniaKontrolaFacade, encje_fasada: FasadaEncji):
    """
    Menu dla niezalogowanego Gościa.
    """
    while True:
        print("\n--- Panel Gościa ---")
        print("1. Przeglądaj katalog książek")
        print("2. Złóż zamówienie (jako Gość)")
        print("3. Wróć do Menu Głównego")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            fasada_kontroli.przegladajKsiazki()

        elif wybor == "2":
            # Logika składania zamówienia przez Gościa
            isbn_list = []
            print("\n--- Składanie Zamówienia (Gość) ---")

            # Wyświetlamy ofertę
            fasada_kontroli.przegladajKsiazki()

            while True:
                isbn_input = input("Podaj ISBN książki do dodania (lub 'k' aby zakończyć): ").strip()
                if isbn_input.lower() == 'k':
                    break
                try:
                    isbn = int(isbn_input)
                    ksiazka = encje_fasada.pobierzPoISBN(isbn)
                    if ksiazka:
                        isbn_list.append(isbn)
                        print(f"Dodano książkę '{ksiazka.tytul}' do zamówienia.")
                    else:
                        print(f"Nie znaleziono książki o ISBN: {isbn}")
                except ValueError:
                    print("Niepoprawny format ISBN.")

            if not isbn_list:
                print("Koszyk pusty. Powrót do menu.")
                continue

            # FINALIZACJA ZAMÓWIENIA DLA GOŚCIA
            print("\n--- Dane do wysyłki (Wymagane do realizacji) ---")
            imie = input("Podaj imię: ")
            nazwisko = input("Podaj nazwisko: ")
            email = input("Podaj email: ")
            adres = input("Podaj adres wysyłki: ")

            # Tworzymy konto tymczasowe
            haslo_tymczasowe = f"guest_{random.randint(1000, 9999)}"

            gosc_klient = Klient(
                imie=imie,
                nazwisko=nazwisko,
                email=email,
                hashHasla=haslo_tymczasowe,
                adresWysylki=adres,
                klientLojalny=False
            )

            # Rejestrujemy go w systemie, aby uzyskał ID
            encje_fasada.rejestrujUzytkownika(gosc_klient)

            print(f"\nGenerowanie zamówienia dla: {imie} {nazwisko}...")
            # Składamy zamówienie używając nowo nadanego ID
            fasada_kontroli.zlozZamowienie(gosc_klient.pobierzId(), isbn_list)
            print("Dziękujemy za zakupy!")

        elif wybor == "3":
            return
        else:
            print("Niepoprawna opcja.")


def menu_klienta(fasada_kontroli: KsiegarniaKontrolaFacade, klient: Klient):
    """
    Wyświetla menu dla Klienta i obsługuje jego opcje (PU04, PU05, PU06, PU03, PU07).
    """
    while True:
        print("\n--- Panel Klienta ---")
        print(f"Zalogowano jako: {klient.imie} {klient.nazwisko}")
        print("1. Przeglądaj katalog książek")  # PU04
        print("2. Złóż nowe zamówienie")  # NOWA OPKJA PU07
        print("3. Przeglądaj historię zakupów")  # PU06
        print("4. Usuń konto (PU03)")
        print("5. Wyloguj")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            fasada_kontroli.przegladajKsiazki()
        elif wybor == "2":
            # dodac aktualizacje historii zamowien
            # PU07: Złożenie zamówienia
            isbn_list = []
            print("\n--- Składanie Zamówienia ---")

            # Wpierw wyświetlamy książki, żeby klient wiedział, co może kupić
            fasada_kontroli.przegladajKsiazki()

            while True:
                isbn_input = input("Podaj ISBN książki do dodania do zamówienia (lub 'k' aby zakończyć): ").strip()
                if isbn_input.lower() == 'k':
                    break
                try:
                    isbn = int(isbn_input)
                    ksiazka = fasada_kontroli._encje_fasada.pobierzPoISBN(isbn)
                    if ksiazka:
                        isbn_list.append(isbn)
                        print(f"Dodano książkę '{ksiazka.tytul}' do zamówienia.")
                    else:
                        print(f"Nie znaleziono książki o ISBN: {isbn}")
                except ValueError:
                    print("Niepoprawny format ISBN. Wprowadź liczbę lub 'k'.")

            if isbn_list:
                print(f"\nPotwierdzanie zamówienia dla {len(isbn_list)} pozycji...")
                fasada_kontroli.zlozZamowienie(klient.pobierzId(), isbn_list)
            else:
                print("Anulowano składanie zamówienia – nie dodano żadnych pozycji.")

        elif wybor == "3":
            # PU06: Pobiera historię zalogowanego klienta
            fasada_kontroli.przegladajHistorie(klient.pobierzId())
        elif wybor == "4":
            # PU03: Usuwanie konta
            fasada_kontroli.usunKonto(klient.pobierzId())
            print("Konto usunięte. Wylogowywanie...")
            return
        elif wybor == "5":
            fasada_kontroli.wylogujUzytkownika()
            print("Wylogowano pomyślnie.")
            return
        else:
            print("Niepoprawna opcja, spróbuj ponownie.")

def menu_administratora(fasada_kontroli: KsiegarniaKontrolaFacade, administrator: Administrator):
    """
    Wyświetla menu dla Administratora i obsługuje jego opcje (PU04, PU05, PU13, PU08-PU12).
    """
    while True:
        print("\n--- Panel Administratora ---")
        print(f"Zalogowano jako: {administrator.imie} {administrator.nazwisko}")

        # Opcje informacyjne i przeglądowe
        print("1. Przeglądaj katalog książek")  # PU04
        print("2. Przeglądaj raporty sprzedażowe (PU13)")

        # Opcje Administracyjne
        print("3. Zarządzaj katalogiem książek (PU08-PU12)")
        print("4. Zarządzaj użytkownikami (PU03)")
        print("5. Wyloguj")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            fasada_kontroli.przegladajKsiazki()
        elif wybor == "2":
            fasada_kontroli.przegladajRaporty()
        elif wybor == "3":
            fasada_kontroli.zarzadzajKatalogiem()
        elif wybor == "4":
            fasada_kontroli.zarzadzajUzytkownikami()
        elif wybor == "5":
            fasada_kontroli.wylogujUzytkownika()
            print("Wylogowano pomyślnie.")
            return
        else:
            print("Niepoprawna opcja, spróbuj ponownie.")


def main():
    print("START")

    print("\nPrzygotowanie danych testowych")
    haslo_test = "haslo123"
    email_test = "uzytkownik@test.pl"

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
        id=1
    )
    encje_fasada.rejestrujUzytkownika(admin_uzytkownik)
    print("Zarejestrowano administratora testowego: admin@test.pl")

    # Tworzenie klienta z pełnymi danymi w main.py (Klient Lojalny - False)
    nowy_klient = Klient(
        imie="TEST",
        nazwisko="Testowa",
        email=email_test,
        hashHasla=haslo_test,
        adresWysylki="ul. Testowa 2",
        klientLojalny=False
    )
    encje_fasada.rejestrujUzytkownika(nowy_klient)
    print(f"Pomyślnie zarejestrowano nowego klienta: {email_test}")

    # Dodanie przykładowych książek do testowania katalogu
    ksiazka1 = fabryka_ksiazek.utworzKsiazke(typ="papierowa", tytul="Wzorce Projektowe", autor="G.O.F", cena=100.0,
                                             ISBN=1000000000000, gatunek="Programowanie", stanMagazynowy=5, opis="Opis 1")
    ksiazka2 = fabryka_ksiazek.utworzKsiazke(typ="ebook", tytul="Czysty Kod", autor="Robert Martin", cena=50.0, ISBN=2000000000000,
                                             gatunek="Programowanie", stanMagazynowy=0, opis="Opis 2",
                                             sciezkaDoPliku="path/to/clean_code.pdf")
    ksiazka3 = fabryka_ksiazek.utworzKsiazke(typ="papierowa", tytul="Zbrodnia i Kara", autor="Fiodor Dostojewski",
                                             cena=35.0, ISBN=3000000000000, gatunek="Klasyka", stanMagazynowy=10, opis="Opis 3")
    encje_fasada.dodajKsiazke(ksiazka1)
    encje_fasada.dodajKsiazke(ksiazka2)
    encje_fasada.dodajKsiazke(ksiazka3)
    print("Dodano przykładowe książki do katalogu.")

    fasada_kontroli = KsiegarniaKontrolaFacade(encje_fasada=encje_fasada)

    print("\nRozpoczęcie interakcji")

    while True:
        print("\n--- Menu Główne ---")
        print("1. Stwórz konto")
        print("2. Zaloguj jako Klient")
        print("3. Zaloguj jako Administrator")
        print("4. Kontynuuj jako Gość")  # <<< NOWA OPCJA
        print("5. Wyjdź z programu")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            # Proces rejestracji (PU01)
            imie = input("Podaj imię: ")
            nazwisko = input("Podaj nazwisko: ")
            email = input("Podaj email: ")
            haslo = input("Podaj hasło: ")
            adres = input("Podaj adres wysyłki: ")

            lista_bledow = []

            if not imie or not imie[0].isupper():
                lista_bledow.append("Imię musi zaczynać się od wielkiej litery i nie może być puste.")

            if not nazwisko or not nazwisko[0].isupper():
                lista_bledow.append("Nazwisko musi zaczynać się od wielkiej litery i nie może być puste.")

            if not email or "@" not in email or "." not in email:
                lista_bledow.append("Email musi mieć poprawny format (musi zawierać @ oraz .).")

            if not haslo:
                lista_bledow.append("Hasło nie może być puste.")

            if not adres:
                lista_bledow.append("Adres nie może być puste.")

            if lista_bledow:
                print("BŁĘDY: ")
                for i, blad in enumerate(lista_bledow, 1):
                    print(f" {i}. {blad}")
                continue

            try:
                klient = Klient(imie, nazwisko, email, haslo, adres, False)
                encje_fasada.rejestrujUzytkownika(klient)
                print(f"Pomyślnie zarejestrowano klienta: {imie} {nazwisko}. Możesz się zalogować.")

            except ValueError as e:
                print(f"\nBŁĄD : {e}")

            continue

        elif wybor == "2":
            # Proces logowania klienta (PU02)
            email_log = input("Email klienta: ")
            haslo_log = input("Hasło klienta: ")
            klient = fasada_kontroli.zalogujKlienta(haslo_log, email_log)
            if klient:
                print("--- Pomyślne logowanie ---")
                menu_klienta(fasada_kontroli, klient)
            else:
                print("Nieprawidłowy login lub hasło klienta.")
        elif wybor == "3":
            # Proces logowania administratora (PU14)
            email_log = input("Email admina: ")
            haslo_log = input("Hasło admina: ")
            admin = fasada_kontroli.zalogujAdministratora(haslo_log, email_log)
            if admin:
                print("--- Pomyślne logowanie ---")
                menu_administratora(fasada_kontroli, admin)
            else:
                print("Nieprawidłowy login lub hasło administratora.")
        elif wybor == "4":
            # Kontynuuj jako Gość
            menu_goscia(fasada_kontroli, encje_fasada)
        elif wybor == "5":
            print("Wyjście z programu.")
            break
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")


if __name__ == "__main__":
    main()