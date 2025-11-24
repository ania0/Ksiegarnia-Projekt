#!/usr/bin/python
# -*- coding: UTF-8 -*-
# from Encje import Zamowienie
# from Encje import Klient
# from Encje import IRepozytoriumZamowien
# from typing import List
#
# class ZamowienieDAO(IRepozytoriumZamowien):
# 	def zapiszZamowienie(self, aZamowienie : Zamowienie):
# 		pass
#
# 	def pobierzHistorieDlaKlienta(self, aIdKlienta : int) -> List:
# 		pass
#
# 	def pobierzWszystkieZamowienia(self) -> List:
# 		pass
#
# 	def obliczCeneOstateczna(self, aZamowienie : Zamowienie, aKlient : Klient) -> float:
# 		pass
#

from typing import List
from encje.IRepozytoriumZamowien import IRepozytoriumZamowien
from encje.Zamowienie import Zamowienie
from encje.Klient import Klient
from encje.MagazynZamowien import MagazynZamowien

# wzorzec, oddzielić logikę dostępu do bazy danych od logiki aplikacji

class ZamowienieDAO(IRepozytoriumZamowien):
    def __init__(self):
        self._magazyn = MagazynZamowien()

    def zapiszZamowienie(self, zamowienie: Zamowienie):
        print("DAO: Zapisuję zamówienie do Magazynu...")
        self._magazyn.dodaj(zamowienie)

    def pobierzHistorieDlaKlienta(self, idKlienta: int) -> List[Zamowienie]:
        return self._magazyn.pobierz_dla_klienta(idKlienta)

    def pobierzWszystkieZamowienia(self) -> List[Zamowienie]:
        return self._magazyn.pobierz_wszystkie()

    def obliczCeneOstateczna(self, zamowienie: Zamowienie, klient: Klient) -> float:
        return zamowienie.obliczCene()