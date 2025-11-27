from abc import ABC, abstractmethod
from encje.ICena import ICena
from encje.Klient import Klient
from typing import Optional


class DekoratorCenyZamowienia(ICena, ABC):
    """
    Abstrakcyjny dekorator ceny zamówienia.
    Dziedziczy po ICena i ABC.
    """

    def __init__(self, komponent: ICena):
        # Obiekt, którego działanie rozszerzamy
        self._komponent: ICena = komponent

    @abstractmethod
    def obliczCene(self) -> float:
        """
        Metoda abstrakcyjna, musi zostać nadpisana w klasach potomnych.
        """
        pass

    def pobierzKlienta(self) -> Optional[Klient]:
        """
        Tymczasowa metoda — sygnatura operacji.
        Zwraca domyślnie None.
        """
        return None
        # lub można też użyć:
        # raise NotImplementedError("pobierzKlienta() nie jest jeszcze zaimplementowane.")
