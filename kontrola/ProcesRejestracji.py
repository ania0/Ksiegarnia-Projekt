from encje.IEncjeFasada import IEncjeFasada
from encje.Uzytkownik import Uzytkownik
import hashlib  # do hashowania haseł


class ProcesRejestracji:
    def __init__(self, fasada_encji: IEncjeFasada, dane: dict):
        """
        :param fasada_encji: Fasada encji do operacji CRUD
        :param dane: Słownik z danymi do rejestracji, np.
                     {"imie": "Anna", "nazwisko": "Kowalska", "login": "anna", "haslo": "123"}
        """
        self._fasada_encji = fasada_encji
        self._dane = dane

    def wykonaj(self):
        print("ProcesRejestracji: Rozpoczynam...")

        login = self._dane.get("login")
        haslo = self._dane.get("haslo")
        imie = self._dane.get("imie", "")
        nazwisko = self._dane.get("nazwisko", "")

        # 1. Sprawdzenie, czy login/email już istnieje
        if self._fasada_encji.czyIstnieje(login):
            print(f"ProcesRejestracji: Użytkownik {login} już istnieje!")
            return None

        # 2. Hashowanie hasła
        hash_hasla = hashlib.sha256(haslo.encode()).hexdigest()

        # 3. Tworzenie obiektu Uzytkownik (dopasowane do Twojej klasy)
        nowy_uzytkownik = Uzytkownik(
            imie=imie,
            nazwisko=nazwisko,
            hashHasla=hash_hasla,
            email=login  # login traktujemy jako email
            # id zostanie przypisane automatycznie przez repozytorium/fasadę TO SPRAWDZIĆ
        )

        # 4. Dodanie do repozytorium przez fasadę
        self._fasada_encji.rejestrujUzytkownika(nowy_uzytkownik)
        print(f"ProcesRejestracji: Użytkownik {login} został zarejestrowany.")
        return nowy_uzytkownik


