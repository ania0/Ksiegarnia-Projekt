#!/usr/bin/python
# -*- coding: UTF-8 -*-
# from abc import ABCMeta, abstractmethod
# from typing import List
#
# class IRepozytoriumKsiazek(object):
# 	"""@Interface"""
# 	__metaclass__ = ABCMeta
# 	@abstractmethod
# 	def dodajKsiazke(self, aKsiazka : IKsiazka):
# 		pass
#
# 	@abstractmethod
# 	def usunKsiazke(self, aIdKsiazki : int):
# 		pass
#
# 	@abstractmethod
# 	def pobierzWszystkie(self) -> List:
# 		pass
#
# 	@abstractmethod
# 	def AktualizujDane(self, aKsiazka : IKsiazka):
# 		pass
#
# 	@abstractmethod
# 	def pobierzPoId(self, aId : int) -> IKsiazka:
# 		pass
#
# 	@abstractmethod
# 	def aktualizujStan(self, aIdKsiazki : int, aNowyStan : int):
# 		pass
#


from typing import List

class IRepozytoriumKsiazek:
    def dodajKsiazke(self, ksiazka: IKsiazka):
        pass

    def usunKsiazke(self, idKsiazki: int):
        pass

    def pobierzWszystkie(self) -> List[IKsiazka]:
        pass

    def AktualizujDane(self, ksiazka: IKsiazka):
        pass

    def pobierzPoId(self, id: int) -> IKsiazka:
        pass

    def aktualizujStan(self, idKsiazki: int, nowyStan: int):
        pass
