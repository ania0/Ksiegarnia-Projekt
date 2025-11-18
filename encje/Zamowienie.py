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
from encje.ICena import ICena
from datetime import date
from typing import List

class Zamowienie(ICena):
    def __init__(self, klient: Klient,
                 data: date, status: str, metodaPlatnosci: str):
        self.klient: Klient = klient
        self.pozycje: List[PozycjaZamowienia] = []
        self.data: date = data
        self.status: str = status
        self.metodaPlatnosci: str = metodaPlatnosci
        self.cenaRazem: foalt = 0.0

    def dodajPozycje(self, pozycja: PozycjaZamowienia):
        self.pozycje.append(pozycja)
        self.obliczCene()

    def obliczCene(self) -> float:
        self.cenaRazem = sum(p.cenaJednostkowa * p.ilosc for p in self.pozycje)
        return self.cenaRazem
