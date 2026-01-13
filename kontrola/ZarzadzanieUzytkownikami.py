from encje.IEncjeFasada import IEncjeFasada
from encje.Administrator import Administrator
from kontrola.ProcesZarzadzania import ProcesZarzadzania
from typing import Optional
from encje.Uzytkownik import Uzytkownik

class ZarzadzanieUzytkownikami(ProcesZarzadzania):
    """
    Proces zarządzania użytkownikami – wersja produkcyjna.
    Pozwala adminowi przeglądać, dodawać, edytować i usuwać użytkowników,
    korzystając wyłącznie z istniejących metod repozytorium.
    """

    def __init__(self, fasada_encji: IEncjeFasada = None, uzytkownik: Administrator = None):
        super().__init__(fasada_encji, uzytkownik)
        self._fasada_encji: IEncjeFasada = fasada_encji
        self._uzytkownik: Administrator = uzytkownik

    def zarzadzajUzytkownikami(self) -> None:
        if not self._fasada_encji or not hasattr(self._fasada_encji, "_repoUzytkownika"):
            print("Brak dostępu do repozytorium użytkowników!")
            return

        repo = self._fasada_encji._repoUzytkownika

        while True:
            # Pobranie aktualnej listy użytkowników
            uzytkownicy = getattr(repo, "_magazyn", [])  # lista z DAO
            print("\nLista użytkowników:")
            for idx, u in enumerate(uzytkownicy, start=1):
                print(f"{idx}. {u.imie} {u.nazwisko} ({u.email}) [ID: {u.pobierzId()}]")

            # Menu opcji
            print("\nOpcje:")
            print("1 - Dodaj użytkownika")
            print("2 - Edytuj użytkownika")
            print("3 - Usuń użytkownika")
            print("4 - Powrót do menu administratora")

            wybor = input("Wybierz opcję: ").strip()

            if wybor == "1":
                # Dodawanie użytkownika
                imie = input("Imię: ").strip()
                nazwisko = input("Nazwisko: ").strip()
                email = input("Email: ").strip()

                if repo.czyIstnieje(email):
                    print("Użytkownik o takim emailu już istnieje!")
                    continue

                haslo = input("Hasło: ").strip()
                adres = input("Adres do wysyłki: ").strip()

                lista_bledow = []

                if not imie: lista_bledow.append("Imię nie może być puste.")
                if not nazwisko: lista_bledow.append("Nazwisko nie może być puste.")
                if not email: lista_bledow.append("Email nie może być pusty.")
                if not haslo: lista_bledow.append("Haslo nie może być puste.")
                if not adres: lista_bledow.append("Adres nie może być pusty.")

                if imie and not imie[0].isupper():
                    lista_bledow.append("Imię musi zaczynać się od wielkiej litery.")

                if nazwisko and not nazwisko[0].isupper():
                    lista_bledow.append("Nazwisko musi zaczynać się od wielkiej litery.")

                if email and ("@" not in email or "." not in email):
                    lista_bledow.append("Email ma niepoprawny format (musi być @ oraz . ).")

                if lista_bledow:
                    print("\nBŁĘDY :")
                    for i, blad in enumerate(lista_bledow, 1):
                        print(f" {i}. {blad}")
                    continue

                try:
                    # Tworzymy obiekt Uzytkownik z wszystkimi danymi
                    nowy = Uzytkownik(imie=imie, nazwisko=nazwisko, email=email)
                    nowy.haslo = haslo
                    nowy.adres = adres

                    repo.rejestrujUzytkownika(nowy)
                    print(f"Użytkownik {imie} {nazwisko} dodany z ID: {nowy.pobierzId()}.")

                except Exception as e:
                    print(f"Wystąpił nieoczekiwany błąd przy zapisie: {e}")

            elif wybor == "2":
                # Edycja użytkownika
                numer = input("Podaj numer użytkownika do edycji: ").strip()
                if not numer.isdigit() or not (1 <= int(numer) <= len(uzytkownicy)):
                    print("Nieprawidłowy numer użytkownika!")
                    continue

                u: Uzytkownik = uzytkownicy[int(numer) - 1]

                print("\n[Modyfikacja danych – Enter = bez zmian]")

                nowe_imie = input(f"Imię [{u.imie}]: ") or None
                nowe_nazwisko = input(f"Nazwisko [{u.nazwisko}]: ") or None
                nowy_email = input(f"Email [{u.email}]: ") or None
                nowe_haslo = input("Nowe hasło: ") or None
                nowy_adres = input("Adres wysyłki: ") or None

                lista_bledow = []

                if nowe_imie and not nowe_imie[0].isupper():
                    lista_bledow.append("Nowe imię musi zaczynać się od wielkiej litery.")

                if nowe_nazwisko and not nowe_nazwisko[0].isupper():
                    lista_bledow.append("Nowe nazwisko musi zaczynać się od wielkiej litery.")

                if nowy_email and ("@" not in nowy_email or "." not in nowy_email):
                    lista_bledow.append("nowy email ma niepoprawny format (musi być @ oraz . ).")

                if nowy_email and repo.czyIstnieje(nowy_email):
                    lista_bledow.append("Email już istnieje – zmiana odrzucona.")

                if lista_bledow:
                    print("\nBŁĘDY :")
                    for i, blad in enumerate(lista_bledow, 1):
                        print(f" {i}. {blad}")
                    continue
                try:
                    self._fasada_encji.aktualizujDaneUzytkownika(
                        uzytkownik=u,
                        noweImie=nowe_imie,
                        noweNazwisko=nowe_nazwisko,
                        nowyEmail=nowy_email,
                        noweHaslo=nowe_haslo,
                        nowyAdres=nowy_adres
                    )

                    print("Dane użytkownika zostały zaktualizowane.")
                except Exception as e:
                    print(f"Wystąpił nieoczekiwany błąd: {e}")


            elif wybor == "3":
                # Usuwanie użytkownika
                numer = input("Podaj numer użytkownika do usunięcia: ").strip()
                if not numer.isdigit() or int(numer) < 1 or int(numer) > len(uzytkownicy):
                    print("Nieprawidłowy numer użytkownika!")
                    continue

                u = uzytkownicy[int(numer) - 1]
                repo.usun(u.pobierzId())
                print("Użytkownik usunięty.")

            elif wybor == "4":
                break
            else:
                print("Nieprawidłowa opcja!")
