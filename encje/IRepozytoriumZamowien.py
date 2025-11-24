from abc import ABC, abstractmethod
from typing import List
from encje.Zamowienie import Zamowienie
from encje.Klient import Klient # Zakładam plik klient.py

class IRepozytoriumZamowien(ABC):
    @abstractmethod
    def zapiszZamowienie(self, zamowienie: Zamowienie): pass

    @abstractmethod
    def pobierzHistorieDlaKlienta(self, idKlienta: int) -> List[Zamowienie]: pass

    @abstractmethod
    def pobierzWszystkieZamowienia(self) -> List[Zamowienie]: pass
