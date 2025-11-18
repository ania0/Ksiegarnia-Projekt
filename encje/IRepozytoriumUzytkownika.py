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

from abc import ABCMeta, abstractmethod
from encje.Uzytkownik import Uzytkownik
from typing import List

class IRepozytoriumUzytkownika(ABC):
    @abstractmethod
    def rejestrujUzytkownika(self, uzytkownik: Uzytkownik):
        pass

    @abstractmethod
    def znajdzUzytkownikaPoEmail(self, email: str) -> Uzytkownik:
        pass

    @abstractmethod
    def czyIstnieje(self, email: str) -> bool:
        pass

    @abstractmethod
    def usun(self, idUzytkownika: int):
        pass

    @abstractmethod
    def pobierzDaneUzytkownika(self, idUzytkownika: int) -> Uzytkownik:
        pass
