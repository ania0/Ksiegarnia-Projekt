# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
# from typing import List
#
# class FabrykaKsiazek(object):
# 	pass

from encje.KsiazkaPapierowa import KsiazkaPapierowa
from encje.Ebook import Ebook
from encje.IKsiazka import IKsiazka  # import interf IKsiazka


# pozwala tworzyć obiekty książek bez bezpośredniego wywoływania konstruktorów konkretnych klas
class FabrykaKsiazek:

    # met tworząca obiekt typu Ebook
    def utworzEbook(self, tytul, autor, ISBN, gatunek, cena, sciezkaDoPliku, opis) -> Ebook:
        return Ebook(tytul, autor, ISBN, gatunek, cena, sciezkaDoPliku, opis)

    # met tworząca obiekt książ papierowej - wymagane przez konstruktor KsiazkaPapierowa
    def utworzKsiazkePapierowa(self, tytul, autor, ISBN, gatunek, cena, stanMagazynowy, opis) -> KsiazkaPapierowa:
        return KsiazkaPapierowa(tytul, autor, ISBN, gatunek, cena, stanMagazynowy, opis)

    def stworzKsiazke(self, tytul: str, autor: str, cena: float):
        pass
