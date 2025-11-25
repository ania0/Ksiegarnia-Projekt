from kontrola.ProcesZarzadzania import ProcesZarzadzania
from encje.IEncjeFasada import IEncjeFasada

"""
class IEncjeFasada(ABC):


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
"""

class ZarzadzanieKsiazkami(ProcesZarzadzania):
    def _wykonajOperacjeNaEncji(self):
        print("ZarzadzanieKsiazkami: Wykonuję operacje na katalogu (Dodaj/Edytuj/Usuń)...")
        raise NotImplementedError("PU: Zarządzanie książkami niezaimplementowane.")