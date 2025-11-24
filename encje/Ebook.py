#!/usr/bin/python
# -*- coding: UTF-8 -*-
# from Encje import iKsiazka
# from typing import List
#
# class Ebook(iKsiazka):
# 	def pobierzCene(self):
# 		pass
#
# 	def __init__(self):
# 		self.___tytul : String = None
# 		self.___autor : String = None
# 		self.___iSBN : int = None
# 		self.___gatunek : String = None
# 		self.___cena : float = None
# 		self.___sciezkaDoPliku : String = None
# 		self.___opis : String = None
#


from encje.IKsiazka import IKsiazka  # import interf książki, po którym dziedziczy Ebook


# kl implementująca interf IKsiazka
class Ebook(IKsiazka):

    # konstruktor Ebook
    def __init__(self, tytul: str, autor: str, ISBN: int, gatunek: str,
                 cena: float, sciezkaDoPliku: str, opis: str):
        self.tytul: str = tytul
        self.autor: str = autor
        self.ISBN: int = ISBN
        self.gatunek: str = gatunek
        self.cena: float = cena
        self.sciezkaDoPliku: str = sciezkaDoPliku
        self.opis: str = opis


    # implementacja met z interf IKsiazka - zwraca cenę e-booka
    def pobierzCene(self) -> float:
        return self.cena
