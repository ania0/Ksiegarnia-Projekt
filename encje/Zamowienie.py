# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
# from Encje import Uzytkownik
# from Encje import ICena
# from typing import List
#
# class Zamowienie(ICena):
# 	def dodajPozycje(self):
# 		pass
#
# 	def obliczCene(self):
# 		pass
#
# 	def __init__(self):
# 		self.___data : date = None
# 		self.___cenaRazem : float = None
# 		self.___uzytkownik : Uzytkownik = None
# 		self.___pozycje : List = None
# 		self.___status : String = None
# 		self.___metodaPlatnosci : String = None
# 		self._unnamed_Uzytkownik_ : Uzytkownik = None
# 		"""# @AssociationMultiplicity 1"""
# 		self._unnamed_PozycjaZamowienia_ = []
# 		"""# @AssociationMultiplicity *"""
#

from encje.Klient import Klient
from encje.PozycjaZamowienia import PozycjaZamowienia
from datetime import date

class Zamowienie:
    def __init__(self, uzytkownik: Klient, pozycje: list[PozycjaZamowienia],
                 data: date, cenaRazem: float, status: str, metodaPlatnosci: str):
        self.uzytkownik = uzytkownik
        self.pozycje = pozycje
        self.data = data
        self.cenaRazem = cenaRazem
        self.status = status
        self.metodaPlatnosci = metodaPlatnosci

    def dodajPozycje(self, pozycja: PozycjaZamowienia):
        self.pozycje.append(pozycja)

    def obliczCene(self) -> float:
        self.cenaRazem = sum(p.cenaJednostkowa * p.ilosc for p in self.pozycje)
        return self.cenaRazem
