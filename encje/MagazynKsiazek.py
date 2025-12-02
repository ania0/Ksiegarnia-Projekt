

# # przechowuje obiekty implementujące IKsiazka
# class MagazynKsiazek:
#
#     def __init__(self):
#         self._ksiazki = []
#
#     def dodaj(self, ksiazka: IKsiazka):
#         self._ksiazki.append(ksiazka)
#
#     def usun(self, id_ksiazki: int):
#         # tworzy nową listę, pomijając książkę o podanym ID
#         self._ksiazki = [k for k in self._ksiazki if getattr(k, 'id', None) != id_ksiazki]
#
#     def pobierz_wszystkie(self):
#         return self._ksiazki
#
#     def znajdz_po_id(self, id: int):
#         # szuka książki o ID
#         for k in self._ksiazki:
#             if getattr(k, 'id', None) == id:
#                 return k
#         # jeśli nie, zwraca None
#         return None
#
#     def aktualizuj(self, ksiazka: IKsiazka):
#         # aktualizuje dane książki w magazynie o ID
#         for i, k in enumerate(self._ksiazki):
#             if getattr(k, 'id', None) == getattr(ksiazka, 'id', None):
#                 self._ksiazki[i] = ksiazka
#                 return

from typing import List
from encje.IKsiazka import IKsiazka

class MagazynKsiazek:

    def __init__(self):
        """# @AssociationKind Aggregation"""
        # lista przechowująca książki w magazynie
        self._listaKsiazek: List[IKsiazka] = []

    # dodatkowe metody pomocnicze (tymczasowo – same sygnatury)
    def pobierzListeKsiazek(self) -> List[IKsiazka]:
        # Zwracamy kopię listy, aby nie pozwolić na bezpośrednią modyfikację
        return self._listaKsiazek.copy()

    def dodaj(self, ksiazka: IKsiazka) -> None:
        self._listaKsiazek.append(ksiazka)

    def usun(self, ISBN: int) -> None:
        self._listaKsiazek = [k for k in self._listaKsiazek if k.ISBN != ISBN]

    def pobierz(self, ISBN: int) -> Optional[IKsiazka]:
        for k in self._listaKsiazek:
            if k.ISBN == ISBN:
                return k
        return None

    # implementacja metod z interfejsu IRepozytoriumKsiazek
#    def dodajKsiazke(self, ksiazka: IKsiazka) -> None:
#        raise NotImplementedError("dodajKsiazke - niezaimplementowane.")
#
#    def usunKsiazke(self, ISBN: int) -> None:
#        raise NotImplementedError("usunKsiazke - niezaimplementowane.")
#
#    def pobierzWszystkie(self) -> List[IKsiazka]:
#        return []
#
#    def AktualizujDane(self, ksiazka: IKsiazka) -> None:
#        raise NotImplementedError("AktualizujDane - niezaimplementowane.")
#
#    def pobierzPoISBN(self, ISBN: int) -> IKsiazka:
#        return None
#
#    def aktualizujStan(self, ISBN: int, nowyStan: int) -> None:
#        raise NotImplementedError("aktualizujStan - niezaimplementowane.")



