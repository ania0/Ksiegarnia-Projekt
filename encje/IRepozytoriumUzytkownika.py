#!/usr/bin/python
# -*- coding: UTF-8 -*-
# from abc import ABCMeta, abstractmethod
# from Encje import Uzytkownik
# from typing import List
#
# class IRepozytoriumUzytkownika(object):
# 	"""@Interface"""
# 	__metaclass__ = ABCMeta
# 	@abstractmethod
# 	def rejestrujUzytkownika(self, aUzytkownik : Class_Diagram___Class_in_a_Package__Airline_.Encje.Uzytkownik):
# 		pass
#
# 	@abstractmethod
# 	def znajdzUzytkownikaPoEmail(self, aEmail : String) -> Uzytkownik:
# 		pass
#
# 	@abstractmethod
# 	def czyIstnieje(self, aEmail : String) -> long:
# 		pass
#
# 	@abstractmethod
# 	def usun(self, aIdUzytkownika : int):
# 		pass
#
# 	@abstractmethod
# 	def pobierzDaneUzytkownika(self, aIdUzytkownika : int) -> Uzytkownik:
# 		pass

from abc import ABC, abstractmethod
from encje.Uzytkownik import Uzytkownik

class IRepozytoriumUzytkownika:
    def rejestrujUzytkownika(self, uzytkownik: Uzytkownik):
        pass

    def znajdzUzytkownikaPoEmail(self, email: str) -> Uzytkownik:
        pass

    def czyIstnieje(self, email: str) -> bool:
        pass

    def usun(self, idUzytkownika: int):
        pass

    def pobierzDaneUzytkownika(self, idUzytkownika: int) -> Uzytkownik:
        pass
