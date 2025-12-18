
from typing import List, Optional
from encje.Zamowienie import Zamowienie


class MagazynZamowien:

    def __init__(self):
        # lista przechowująca zamówienia
        self._listaZamowien: List[Zamowienie] = []
        """# @AssociationKind Aggregation"""

    def pobierzListeZamowien(self) -> List[Zamowienie]:
        return self._listaZamowien

    def dodaj(self, zamowienie: Zamowienie) -> None:
        self._listaZamowien.append(zamowienie)

    def pobierz(self, id: int) -> Optional[Zamowienie]:
        for z in self._listaZamowien:
            if z.id == id:
                return z
        return None

