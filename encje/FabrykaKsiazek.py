

from typing import List
from encje.KsiazkaPapierowa import KsiazkaPapierowa
from encje.Ebook import Ebook
from encje.IKsiazka import IKsiazka

class FabrykaKsiazek:
	def utworzKsiazke(self, typ: str, tytul: str, autor: str, cena: float, ISBN:int, gatunek: str, stanMagazynowy:int, opis: str, sciezkaDoPliku: str = "") -> IKsiazka:
		"""
        Tworzy książkę w zależności od typu:
        - "papierowa" → KsiazkaPapierowa
        - "ebook" → Ebook
        """
		typ = typ.lower()
		if typ == "papierowa":
			return KsiazkaPapierowa(tytul=tytul, autor=autor, ISBN=ISBN, gatunek=gatunek, cena=cena, stanMagazynowy=stanMagazynowy, opis=opis)
		elif typ == "ebook":
			return Ebook(tytul=tytul, autor=autor, ISBN=ISBN, gatunek=gatunek, cena=cena, sciezkaDoPliku=sciezkaDoPliku, opis=opis)
		else:
			raise ValueError(f"Nieobsługiwany typ książki: {typ}")

