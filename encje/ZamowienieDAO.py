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


from encje.IRepozytoriumZamowien import IRepozytoriumZamowien
from encje.Zamowienie import Zamowienie
from encje.Klient import Klient
from typing import List

class ZamowienieDAO(IRepozytoriumZamowien):
    def __init__(self):
        self.zamowienia: List[Zamowienie] = []

    def zapiszZamowienie(self, zamowienie: Zamowienie):
        self.zamowienia.append(zamowienie)

    def pobierzHistorieDlaKlienta(self, idKlienta: int) -> List[Zamowienie]:
        return [z for z in self.zamowienia if z.uzytkownik.id == idKlienta]

    def pobierzWszystkieZamowienia(self) -> List[Zamowienie]:
        return self.zamowienia

    def obliczCeneOstateczna(self, zamowienie: Zamowienie, klient: Klient) -> float:
        # W tym miejscu można zastosować dekoratory rabatów itp.
        return zamowienie.obliczCene()
