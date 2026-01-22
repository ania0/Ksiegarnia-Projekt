from typing import List
from abc import ABC, abstractmethod
from encje.IKsiazka import IKsiazka

# jakie operacje klasa repozytorium ma dostarczyc
class IRepozytoriumKsiazek(ABC):

    @abstractmethod
    def dodajKsiazke(self, Ksiazka: IKsiazka) -> None:
        pass

    @abstractmethod
    def usunKsiazke(self, ISBN: int) -> None:
        pass

    @abstractmethod
    def pobierzWszystkie(self) -> List[IKsiazka]:
        pass

    @abstractmethod
    def aktualizujDane(self, Ksiazka: IKsiazka) -> None:
        pass

    @abstractmethod
    def pobierzPoISBN(self, ISBN: int) -> IKsiazka:
        pass

    @abstractmethod
    def aktualizujStan(self, ISBN: int, NowyStan: int) -> None:
        pass

    @abstractmethod
    def pobierzWszystkie(self) -> List[IKsiazka]:
        pass