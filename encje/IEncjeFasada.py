from abc import ABC, abstractmethod  # klasy do tworzenia interfejsów i metod abstrakcyjnych
from typing import List  # do typowania list
from encje.Uzytkownik import Uzytkownik
from encje.Klient import Klient
from encje.Zamowienie import Zamowienie
from encje.IKsiazka import IKsiazka


# Interf fasady dla encji – zestaw metod, które fasada musi udostępniać
# Klient używa fasady, zamiast bezpośrednio kontaktować się z repozytoriami
# Met abstrakt wymuszają implementację w kl dziedziczących
class IEncjeFasada(ABC):

    @abstractmethod
    def rejestrujUzytkownika(self, uzytkownik: Uzytkownik):
        pass

    @abstractmethod
    def znajdzUzytkownikaPoEmailu(self, email: str) -> Uzytkownik:
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


    @abstractmethod
    def dodajKsiazke(self, ksiazka: IKsiazka):
        pass

    @abstractmethod
    def usunKsiazke(self, ISBN: int):
        pass

    @abstractmethod
    def pobierzWszystkie(self) -> List[IKsiazka]:
        pass

    @abstractmethod
    def aktualizujDane(self, ksiazka: IKsiazka):
        pass

    @abstractmethod
    def pobierzPoISBN(self, ISBN : int) -> IKsiazka:
        pass

    @abstractmethod
    def aktualizujStan(self, ISBN: int, nowyStan: int):
        pass

    @abstractmethod
    def zapiszZamowienie(self, zamowienie: Zamowienie):
        pass

    @abstractmethod
    def pobierzHistorieDlaKlienta(self, idKlienta: int) -> List[Zamowienie]:
        pass

    @abstractmethod
    def pobierzWszystkieZamowienia(self) -> List[Zamowienie]:
        pass

    @abstractmethod
    def obliczCeneOstateczna(self, zamowienie: Zamowienie, klient: Klient) -> float:
        # laczy encje zamówienie + klient
        # moze zastosować dekoratory
        pass
