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

                nowy = Uzytkownik(imie=imie, nazwisko=nazwisko, email=email)
                repo.rejestrujUzytkownika(nowy)
                print(f"Użytkownik {imie} {nazwisko} dodany z ID: {nowy.pobierzId()}.")

            elif wybor == "2":
                # Edycja użytkownika
                numer = input("Podaj numer użytkownika do edycji: ").strip()
                if not numer.isdigit() or int(numer) < 1 or int(numer) > len(uzytkownicy):
                    print("Nieprawidłowy numer użytkownika!")
                    continue

                u = uzytkownicy[int(numer) - 1]
                nowe_imie = input(f"Nowe imię ({u.imie}): ").strip()
                nowe_nazwisko = input(f"Nowe nazwisko ({u.nazwisko}): ").strip()
                nowe_email = input(f"Nowy email ({u.email}): ").strip()

                if nowe_imie:
                    u.imie = nowe_imie
                if nowe_nazwisko:
                    u.nazwisko = nowe_nazwisko
                if nowe_email:
                    if repo.czyIstnieje(nowe_email):
                        print("Email już istnieje, zmiana odrzucona!")
                    else:
                        u.email = nowe_email

                print("Dane użytkownika zaktualizowane.")

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
