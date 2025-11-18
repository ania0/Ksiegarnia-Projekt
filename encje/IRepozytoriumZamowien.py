#!/usr/bin/python
# -*- coding: UTF-8 -*-
# from abc import ABCMeta, abstractmethod
# from Encje import Zamowienie
# from Encje import Klient
# from typing import List
#
# class IRepozytoriumZamowien(object):
# 	"""@Interface"""
# 	__metaclass__ = ABCMeta
# 	@abstractmethod
# 	def zapiszZamowienie(self, aZamowienie : Zamowienie):
# 		pass
#
# 	@abstractmethod
# 	def pobierzHistorieDlaKlienta(self, aIdKlienta : int) -> List:
# 		pass
#
# 	@abstractmethod
# 	def pobierzWszystkieZamowienia(self) -> List:
# 		pass
#
# 	@abstractmethod
# 	def obliczCeneOstateczna(self, aZamowienie : Zamowienie, aKlient : Klient) -> float:
# 		pass
#

from encje.Zamowienie import Zamowienie
from encje.Klient import Klient
from typing import List

class IRepozytoriumZamowien:
    def zapiszZamowienie(self, zamowienie: Zamowienie):
        pass

    def pobierzHistorieDlaKlienta(self, idKlienta: int) -> List[Zamowienie]:
        pass

    def pobierzWszystkieZamowienia(self) -> List[Zamowienie]:
        pass

    def obliczCeneOstateczna(self, zamowienie: Zamowienie, klient: Klient) -> float:
        pass
