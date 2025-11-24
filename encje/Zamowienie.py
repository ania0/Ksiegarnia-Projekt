from typing import List
from datetime import date
from encje.Klient import Klient
from encje.PozycjaZamowienia import PozycjaZamowienia
from encje.ICena import ICena

class Zamowienie(ICena):
    def __init__(self, klient: Klient, data: date, status: str, metodaPlatnosci: str):
        self.klient: Klient = klient
        # Relacja: Zamówienie zawiera listę Pozycji
        self.pozycje: List[PozycjaZamowienia] = []
        self.data: date = data
        self.status: str = status
        self.metodaPlatnosci: str = metodaPlatnosci
        self.cenaRazem: float = 0.0

    def dodajPozycje(self, pozycja: PozycjaZamowienia):
        self.pozycje.append(pozycja)
        # Automatyczne przeliczenie ceny po dodaniu
        self.obliczCene()

    # Implementacja metody z interfejsu ICena
    def obliczCene(self) -> float:
        # ilość * cena dla każdej pozycji
        return sum(p.ilosc * p.cenaJednostkowa for p in self.pozycje)