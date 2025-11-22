# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
# from typing import List
#
# class FabrykaKsiazek(object):
# 	pass

from encje.KsiazkaPapierowa import KsiazkaPapierowa
from encje.Ebook import Ebook
from encje.IKsiazka import IKsiazka

# tworzenie obiektow ksiazek
# fabryka - nie trzeba znac konstruktorow konkretnych klas

class FabrykaKsiazek:
    def utworzEbook(self, tytul, autor, ISBN, gatunek, cena, sciezkaDoPliku, opis) -> Ebook:
        return Ebook(tytul, autor, ISBN, gatunek, cena, sciezkaDoPliku, opis)

    def utworzKsiazkePapierowa(self, tytul, autor, ISBN, gatunek, cena, stanMagazynowy, opis) -> KsiazkaPapierowa:
        return KsiazkaPapierowa(tytul, autor, ISBN, gatunek, cena, stanMagazynowy, opis)