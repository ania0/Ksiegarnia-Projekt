#!/usr/bin/python
# -*- coding: UTF-8 -*-
# from Encje import IRepozytoriumKsiazek
# from typing import List
#
# class KsiazkaDAO(IRepozytoriumKsiazek):
# 	def dodajKsiazke(self, aKsiazka : IKsiazka):
# 		pass
#
# 	def usunKsiazke(self, aIdKsiazki : int):
# 		pass
#
# 	def pobierzWszystkie(self) -> List:
# 		pass
#
# 	def AktualizujDane(self, aKsiazka : IKsiazka):
# 		pass
#
# 	def pobierzPoId(self, aId : int) -> IKsiazka:
# 		pass
#
# 	def aktualizujStan(self, aIdKsiazki : int, aNowyStan : int):
# 		pass


from encje.IKsiazka import IKsiazka
from encje.IRepozytoriumKsiazek import IRepozytoriumKsiazek
from encje.KsiazkaPapierowa import KsiazkaPapierowa
from typing import List

class KsiazkaDAO(IRepozytoriumKsiazek):
    def __init__(self):
        self.listaKsiazek: List[IKsiazka] = []

    def dodajKsiazke(self, ksiazka: IKsiazka):
        self.listaKsiazek.append(ksiazka)

    def usunKsiazke(self, idKsiazki: int):
        self.listaKsiazek = [k for k in self.listaKsiazek if getattr(k, 'id', None) != idKsiazki]

    def pobierzWszystkie(self) -> List[IKsiazka]:
        return self.listaKsiazek

    def AktualizujDane(self, ksiazka: IKsiazka):
        for i, k in enumerate(self.listaKsiazek):
            if getattr(k, 'id', None) == getattr(ksiazka, 'id', None):
                self.listaKsiazek[i] = ksiazka

    def pobierzPoId(self, id: int) -> IKsiazka:
        for k in self.listaKsiazek:
            if getattr(k, 'id', None) == id:
                return k
        return None

    def aktualizujStan(self, idKsiazki: int, nowyStan: int):
        k = self.pobierzPoId(idKsiazki)
        if k:
            k.stanMagazynowy = nowyStan

