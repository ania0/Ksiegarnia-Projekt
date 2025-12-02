# from kontrola.IStrategiaUwierzytelniania import IStrategiaUwierzytelniania
# from encje.Uzytkownik import Uzytkownik
# from typing import Optional
#
#
# class KontekstUwierzytelniania:
#     def __init__(self):
#         self._strategia = None
#         self._zalogowanyUzytkownik = None
#
#     def ustawStrategie(self, strategia: IStrategiaUwierzytelniania):
#         self._strategia = strategia
#
#     def wykonajUwierzytelnianie(self, login: str, haslo: str):
#         if not self._strategia:
#             print("Błąd: Nie ustawiono strategii logowania.")
#             return None
#
#     def getZalogowanyUzytkownik(self) -> Optional[Uzytkownik]:
#         return self._zalogowanyUzytkownik
#
#         self._zalogowanyUzytkownik = self._strategia.uwierzytelnij(login, haslo)
#
#         if self._zalogowanyUzytkownik:
#             print(f"Kontekst: Zalogowano użytkownika: {self._zalogowanyUzytkownik.login}")
#         else:
#             print("Kontekst: Nieudane logowanie.")
#
#         return self._zalogowanyUzytkownik
#
#
from typing import Optional
from encje.Uzytkownik import Uzytkownik
from kontrola.IStrategiaUwierzytelniania import IStrategiaUwierzytelniania
#from kontrola.KsiegarniaKontrolaFacade import KsiegarniaKontrolaFacade


#from kontrola.KsiegarniaKontrolaFacade import KsiegarniaKontrolaFacade


class KontekstUwierzytelniania:


    def __init__(self):
        # Strategia uwierzytelniania (asocjacja 1..1)
        self._strategia: IStrategiaUwierzytelniania = None
        # Zalogowany użytkownik (asocjacja 0..1)
        self._zalogowanyUzytkownik: Uzytkownik = None
        # Asocjacja z fasadą (warstwa kontroli)
        from kontrola.KsiegarniaKontrolaFacade import KsiegarniaKontrolaFacade  # tu żeby zapobiec cross import
        self._fasadaKontroli: KsiegarniaKontrolaFacade = None # tu nie jestem pewwna czy jest wystarczajaca ilosc atrybutow
        self._zalogowanyUzytkownik = None

    def ustawStrategie(self, strategia: IStrategiaUwierzytelniania) -> None:
        """
        Ustawia strategię uwierzytelniania.
        """
        self._strategia = strategia

    def wykonajUwierzytelnianie(self, email: str, hashHasla: str) -> Optional[Uzytkownik]:
        """
        Wykonuje uwierzytelnianie przy użyciu aktualnej strategii.
        """
        if self._strategia is None:
            raise ValueError("Nie ustawiono strategii uwierzytelniania.")

        # Strategia zwraca użytkownika jeśli dane są poprawne, w przeciwnym wypadku None
        uzytkownik = self._strategia.uwierz(email, hashHasla)
        self._zalogowanyUzytkownik = uzytkownik
        return uzytkownik

    def getZalogowanyUzytkownik(self) -> Optional[Uzytkownik]:
        """
        Zwraca aktualnie zalogowanego użytkownika.
        """
        return self._zalogowanyUzytkownik
