# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
# from Encje import Zamowienie
# from Encje import iKsiazka
# from typing import List
#
# class PozycjaZamowienia(object):
# 	def __init__(self):
# 		self.___ilosc : int = None
# 		self.___cenaJednostkowa : int = None
# 		self.___ksiazka : Iksiazka = None
# 		self._unnamed_Zamowienie_ : Zamowienie = None
# 		"""# @AssociationMultiplicity 1"""
# 		self._unnamed_iKsiazka_ : iKsiazka = None
# 		"""# @AssociationMultiplicity 1"""
#

from encje.IKsiazka import IKsiazka
from encje.Zamowienie import Zamowienie
from typing import Union

class PozycjaZamowienia:
    def __init__(self, ksiazka: IKsiazka, ilosc: int, cenaJednostkowa: float):
        self.ksiazka: IKsiazka = ksiazka
        self.ilosc: int = ilosc
        self.cenaJednostkowa: float = cenaJednostkowa
