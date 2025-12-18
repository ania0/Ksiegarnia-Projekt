from typing import Optional
from encje.Uzytkownik import Uzytkownik
from kontrola.IStrategiaUwierzytelniania import IStrategiaUwierzytelniania

class KontekstUwierzytelniania:


    def __init__(self):
        # Strategia uwierzytelniania (asocjacja 1..1)
        self._strategia: IStrategiaUwierzytelniania = None
        # Zalogowany użytkownik (asocjacja 0..1)
        self._zalogowanyUzytkownik: Uzytkownik = None
        # Asocjacja z fasadą (warstwa kontroli)
        from kontrola.KsiegarniaKontrolaFacade import KsiegarniaKontrolaFacade  # tu żeby zapobiec cross import
        self._fasadaKontroli: KsiegarniaKontrolaFacade = None # tu nie jestem pewwna czy jest wystarczajaca ilosc atrybutow
        #self._zalogowanyUzytkownik = None

    def ustawStrategie(self, strategia: IStrategiaUwierzytelniania) -> None:
        """
        Ustawia strategię uwierzytelniania.
        """
        self._strategia = strategia

    def wykonajUwierzytelnianie(self, email: str, haslo: str) -> Optional[Uzytkownik]:
        """
        Wykonuje uwierzytelnianie przy użyciu aktualnej strategii.
        """
        if self._strategia is None:
            raise ValueError("Nie ustawiono strategii uwierzytelniania.")

        # Strategia zwraca użytkownika jeśli dane są poprawne, w przeciwnym wypadku None
        uzytkownik = self._strategia.uwierzytelnij(email, haslo)
        self._zalogowanyUzytkownik = uzytkownik
        return uzytkownik

    def wyloguj(self) -> None:
        """
        Wylogowuje użytkownika, czyszcząc pole zalogowanyUzytkownik.
        """
        self._zalogowanyUzytkownik = None

    def getZalogowanyUzytkownik(self) -> Optional[Uzytkownik]:
        """
        Zwraca aktualnie zalogowanego użytkownika.
        """
        return self._zalogowanyUzytkownik
