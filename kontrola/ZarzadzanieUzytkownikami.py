from kontrola.ProcesZarzadzania import ProcesZarzadzania
from encje.IEncjeFasada import IEncjeFasada
from encje.Uzytkownik import Uzytkownik

"""
class IEncjeFasada(ABC):


    @abstractmethod
    def rejestrujUzytkownika(self, uzytkownik: Uzytkownik):
        pass

    @abstractmethod
    def znajdzUzytkownikaPoLoginie(self, email: str) -> Uzytkownik:
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
"""

from encje.IEncjeFasada import IEncjeFasada
from encje.Administrator import Administrator
from kontrola.ProcesZarzadzania import ProcesZarzadzania
from typing import Optional


class ZarzadzanieUzytkownikami(ProcesZarzadzania):
    """
    Proces zarządzania użytkownikami – wersja szkieletowa.
    Dziedziczy po ProcesZarzadzania.
    """

    def __init__(self, fasada_encji: IEncjeFasada = None, uzytkownik: Administrator = None):
        super().__init__(fasada_encji, uzytkownik)
        # Pola klasy (związki z encjami i użytkownikiem)
        self._fasada_encji: IEncjeFasada = fasada_encji
        self._uzytkownik: Administrator = uzytkownik

    def zarzadzajUzytkownikami(self) -> None:
        # Tymczasowa logika testowa: wypisanie listy użytkowników
        uzytkownicy = self._fasada_encji.pobierzWszystkichUzytkownikow() if self._fasada_encji else []
        print("Zarządzanie użytkownikami – lista dostępnych użytkowników:")
        for u in uzytkownicy:
            print(
                f"- {getattr(u, 'imie', 'Brak imienia')} {getattr(u, 'nazwisko', 'Brak nazwiska')} ({getattr(u, 'email', 'Brak email')})")
        print("PU: Logika dodawania/edycji/usuwania użytkowników nie jest jeszcze zaimplementowana.")
