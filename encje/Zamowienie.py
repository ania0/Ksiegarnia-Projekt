from typing import List, Optional
from datetime import date
from encje.ICena import ICena
from encje.Klient import Klient
from encje.PozycjaZamowienia import PozycjaZamowienia


class Zamowienie(ICena):
    """
    Klasa domenowa Zamowienie – na tym etapie zawiera tylko strukturę,
    deklarację atrybutów i sygnatury operacji bez implementacji.
    """

    def __init__(self):
        # Atrybuty podstawowe
        self._data: Optional[date] = None
        self._cenaRazem: Optional[float] = None
        self._status: Optional[str] = None
        self._metodaPlatnosci: Optional[str] = None
        self._id: Optional[int] = None

        # Asocjacja 1..1 z Klientem
        self._klient: Klient = None

        # Kompozycja: * PozycjaZamowienia
        self._pozycjeZamowienia: List[PozycjaZamowienia] = []
        # @AssociationMultiplicity *
        # @AssociationKind Composition


    def dodajPozycje(self, pozycja: PozycjaZamowienia) -> None:
        """Dodaje pozycję do zamówienia i przelicza cenę."""
        self._pozycjeZamowienia.append(pozycja)

    def obliczCene(self) -> float:
        """Oblicza sumaryczną cenę zamówienia na podstawie pozycji."""
        return sum(p.ilosc * p.cenaJednostkowa for p in self._pozycjeZamowienia)

    def pobierzId(self) -> int:
        """Zwraca ID zamówienia."""
        return self._id

    def pobierzKlienta(self) -> Optional[Klient]:
        """Zwraca klienta powiązanego z zamówieniem."""
        return self._klient
