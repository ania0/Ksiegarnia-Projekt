from typing import List
from datetime import date
from encje.Klient import Klient
from encje.Uzytkownik import Uzytkownik
from encje.PozycjaZamowienia import PozycjaZamowienia
from encje.ICena import ICena

# class Zamowienie(ICena):
#     def __init__(self, uzytkownik: Uzytkownik, data: date, status: str, metodaPlatnosci: str):
#         self.uzytkownik : Uzytkownik = None
#         # Relacja: Zamówienie zawiera listę Pozycji
#         self.pozycje: List[PozycjaZamowienia] = []
#         self.data: date = data
#         self.status: str = status
#         self.metodaPlatnosci: str = metodaPlatnosci
#         self.cenaRazem: float = 0.0
#
#     def dodajPozycje(self, pozycja: PozycjaZamowienia):
#         self.pozycje.append(pozycja)
#         # Automatyczne przeliczenie ceny po dodaniu
#         self.obliczCene()
#
#     # Implementacja metody z interfejsu ICena
#     def obliczCene(self) -> float:
#         # ilość * cena dla każdej pozycji
#         return sum(p.ilosc * p.cenaJednostkowa for p in self.pozycje)

# class Zamowienie(ICena):
#         def dodajPozycje(self) -> None:
#             pass
#
#         def obliczCene(self) -> float:
#             pass
#
#         def pobierzId(self) -> int:
#             pass
#
#         def pobierzKlienta(self) -> Klient:
#             pass
#
#         def __init__(self):
#             self._data: date = None
#             self._cenaRazem: float = None
#             self._uzytkownik: Uzytkownik = None
#             self._pozycje: List = None
#             self._status: str = None
#             self._metodaPlatnosci: str = None
#             self._id: int = None
#             # self._unnamed_MagazynZamowien_45: MagazynZamowien = None
#             self._unnamed_Klient_: Klient = None
#             """# @AssociationMultiplicity 0..1"""
#             self._unnamed_PozycjaZamowienia_ = []
#             """# @AssociationMultiplicity *
#             # @AssociationKind Composition"""


from typing import List, Optional
from datetime import date
from encje.ICena import ICena
from encje.Klient import Klient
from encje.Uzytkownik import Uzytkownik
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
        self._uzytkownik: Optional[Uzytkownik] = None
        self._pozycje: List[PozycjaZamowienia] = []   # kompozycja
        self._status: Optional[str] = None
        self._metodaPlatnosci: Optional[str] = None
        self._id: Optional[int] = None

        # Asocjacja 0..1 z Klientem
        self._klient: Optional[Klient] = None

        # Kompozycja: * PozycjaZamowienia
        self._pozycjeZamowienia: List[PozycjaZamowienia] = []
        # @AssociationMultiplicity *
        # @AssociationKind Composition


    def dodajPozycje(self) -> None:
        raise NotImplementedError("dodajPozycje() nie jest jeszcze zaimplementowane.")

    def obliczCene(self) -> float:
        # metoda zwracająca wartość domyślną
        return 0.0

    def pobierzId(self) -> int:
        return 0  # domyślna wartość

    def pobierzKlienta(self) -> Klient:
        return None  # domyślna wartość
