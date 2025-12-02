# from encje.Zamowienie import Zamowienie
#
# class MagazynZamowien:
#     def __init__(self):
#         self._zamowienia = []
#
#     def dodaj(self, zamowienie: Zamowienie):
#         self._zamowienia.append(zamowienie)
#
#     def pobierz_wszystkie(self):
#         return self._zamowienia
#
#     def pobierz_dla_klienta(self, id_klienta: int):
#         return [z for z in self._zamowienia if getattr(z.uzytkownik, 'id', None) == id_klienta]


from typing import List
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

#    def usun(self, id: int) -> None:   # po co nam usuwanie zamówień??
#        raise NotImplementedError("usun - niezaimplementowane.")


    # metody z interfejsu IRepozytoriumZamowien
#   def zapiszZamowienie(self, zamowienie: Zamowienie) -> None:
#        raise NotImplementedError("zapiszZamowienie - niezaimplementowane.")
#
#    def pobierzHistorieDlaKlienta(self, id: int) -> List[Zamowienie]:
#        return []
#
#    def pobierzWszystkieZamowienia(self) -> List[Zamowienie]:
#        return []
