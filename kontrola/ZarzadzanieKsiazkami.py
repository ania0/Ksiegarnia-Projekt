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
#
# class ZarzadzanieKsiazkami(ProcesZarzadzania):
#     def _wykonajOperacjeNaEncji(self):
#         print("ZarzadzanieKsiazkami: Wykonuję operacje na katalogu (Dodaj/Edytuj/Usuń)...")
#         raise NotImplementedError("PU: Zarządzanie książkami niezaimplementowane.")

from encje.IEncjeFasada import IEncjeFasada
from encje.Administrator import Administrator
from kontrola.ProcesZarzadzania import ProcesZarzadzania
from typing import Optional


class ZarzadzanieKsiazkami(ProcesZarzadzania):
    """
    Proces zarządzania książkami – wersja szkieletowa.
    Dziedziczy po ProcesZarzadzania.
    """

    def __init__(self, fasada_encji: Optional[IEncjeFasada] = None, uzytkownik: Optional[Administrator] = None):
        super().__init__(fasada_encji, uzytkownik)
        # Pola klasy (związki z encjami i użytkownikiem)
        self._fasada_encji: Optional[IEncjeFasada] = fasada_encji
        self._uzytkownik: Optional[Administrator] = uzytkownik

        def zarzadzajKsiazkami(self) -> None:
            # Tymczasowa logika testowa: np. pobranie listy książek i wypisanie tytułów
            ksiazki = self._fasada_encji.pobierzWszystkie() if self._fasada_encji else []
            print("Zarządzanie książkami – lista dostępnych książek:")
            for k in ksiazki:
                print(f"- {getattr(k, 'tytul', 'Brak tytułu')}")
            print("PU: Logika dodawania/edycji/usuwania książek nie jest jeszcze zaimplementowana.")

