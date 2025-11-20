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


# przechowywanie i pobieraniem obiektow Zamowienie
# dziedziczy po IRepozytoriumZamowien - musi implementować metody

# wzorzec projektowy do oddzielania logiki dostępu do danych od reszty aplikacji
class ZamowienieDAO(IRepozytoriumZamowien):
    def __init__(self):
        self.listaZamowien: List[Zamowienie] = []

    def zapiszZamowienie(self, zamowienie: Zamowienie):
        self.listaZamowien.append(zamowienie)


# zwraca liste zamowien klienta, po idKlienta
    def pobierzHistorieDlaKlienta(self, idKlienta: int) -> List[Zamowienie]:
        return [z for z in self.listaZamowien if z.uzytkownik.id == idKlienta]

    def pobierzWszystkieZamowienia(self) -> List[Zamowienie]:
        return self.listaZamowien

    def obliczCeneOstateczna(self, zamowienie: Zamowienie, klient: Klient) -> float:
        return zamowienie.obliczCene()
