# from encje.KsiazkaPapierowa import KsiazkaPapierowa
# from encje.Ebook import Ebook
#
#
# class FabrykaKsiazek:
#
#     def utworzEbook(self, tytul, autor, ISBN, gatunek, cena, sciezkaDoPliku, opis) -> Ebook:
#         # tylko sygnatura
#         raise NotImplementedError()
#
#     def utworzKsiazkePapierowa(self, tytul, autor, ISBN, gatunek, cena, stanMagazynowy, opis) -> KsiazkaPapierowa:
#         # tylko sygnatura
#         raise NotImplementedError()
#
#     def stworzKsiazke(self, tytul: str, autor: str, cena: float):
#         # tylko sygnatura
#         raise NotImplementedError()

from typing import List
from encje.KsiazkaPapierowa import KsiazkaPapierowa
from encje.Ebook import Ebook
from encje.IKsiazka import IKsiazka

class FabrykaKsiazek:
	def utworzKsiazke(self, typ : str, tytul : str, autor : str, cena : float) -> IKsiazka:
		pass


