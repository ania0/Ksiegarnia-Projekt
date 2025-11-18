#!/usr/bin/python
# -*- coding: UTF-8 -*-
# from Encje import iKsiazka
# from typing import List
#
# class KsiazkaPapierowa(iKsiazka):
# 	def pobierzCene(self):
# 		pass
#
# 	def __init__(self):
# 		self.___tytul : String = None
# 		self.___autor : String = None
# 		self.___iSBN : int = None
# 		self.___gatunek : String = None
# 		self.___cena : float = None
# 		self.___stanMagazynowy : int = None
# 		self.___opis : String = None
#


class KsiazkaPapierowa:
    def __init__(self, tytul: str, autor: str, ISBN: int, gatunek: str,
                 cena: float, stanMagazynowy: int, opis: str):
        self.tytul = tytul
        self.autor = autor
        self.ISBN = ISBN
        self.gatunek = gatunek
        self.cena = cena
        self.stanMagazynowy = stanMagazynowy
        self.opis = opis

    def pobierzCene(self) -> float:
        return self.cena
