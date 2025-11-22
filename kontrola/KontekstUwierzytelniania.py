from kontrola.IStrategiaUwierzytelniania import IStrategiaUwierzytelniania
from encje.Uzytkownik import Uzytkownik


class KontekstUwierzytelniania:
    def __init__(self):
        self._strategia = None
        self._zalogowanyUzytkownik = None

    def ustawStrategie(self, strategia: IStrategiaUwierzytelniania):
        self._strategia = strategia

    def wykonajUwierzytelnianie(self, login: str, haslo: str):
        if not self._strategia:
            print("Błąd: Nie ustawiono strategii logowania.")
            return None

        self._zalogowanyUzytkownik = self._strategia.uwierzytelnij(login, haslo)

        if self._zalogowanyUzytkownik:
            print(f"Kontekst: Zalogowano użytkownika: {self._zalogowanyUzytkownik.login}")
        else:
            print("Kontekst: Nieudane logowanie.")

        return self._zalogowanyUzytkownik

    def getZalogowanyUzytkownik(self) -> Uzytkownik:
        return self._zalogowanyUzytkownik