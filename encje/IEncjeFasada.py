# #!/usr/bin/python



from abc import ABC, abstractmethod
from typing import List
from encje.Uzytkownik import Uzytkownik
from encje.Klient import Klient
from encje.Zamowienie import Zamowienie
from encje.IKsiazka import IKsiazka

class IEncjeFasada(ABC):

    # Uzytkownicy
    # klient moze wykonac operacje na uzyt przez jedna klase
    # dekorator
    # klasa dziedziczaca musi zaimplementowac metode
    @abstractmethod
    def rejestrujUzytkownika(self, uzytkownik: Uzytkownik):
        pass

    @abstractmethod
    def znajdzUzytkownikaPoEmail(self, email: str) -> Uzytkownik:
        pass

    @abstractmethod
    def czyIstnieje(self, email: str) -> bool:
        pass

    @abstractmethod
    def usun(self, idUzytkownika: int):
        pass

    @abstractmethod
    def pobierzDaneUzytkownika(self, idUzytkownika: int) -> Uzytkownik:
        pass

    # Ksiazki
    @abstractmethod
    def dodajKsiazke(self, ksiazka: IKsiazka):
        pass

    @abstractmethod
    def usunKsiazke(self, idKsiazki: int):
        pass

    @abstractmethod
    def pobierzWszystkie(self) -> List[IKsiazka]:
        pass

    @abstractmethod
    def aktualizujDane(self, ksiazka: IKsiazka):
        pass

    @abstractmethod
    def pobierzPoId(self, id: int) -> IKsiazka:
        pass

    @abstractmethod
    def aktualizujStan(self, idKsiazki: int, nowyStan: int):
        pass

    # Zamowienia
    @abstractmethod
    def zapiszZamowienie(self, zamowienie: Zamowienie):
        pass

    @abstractmethod
    def pobierzHistorieDlaKlienta(self, idKlienta: int) -> List[Zamowienie]:
        pass

    @abstractmethod
    def pobierzWszystkieZamowienia(self) -> List[Zamowienie]:
        pass

    #laczy wiecej niz jedna encje
    @abstractmethod
    def obliczCeneOstateczna(self, zamowienie: Zamowienie, klient: Klient) -> float:
        pass