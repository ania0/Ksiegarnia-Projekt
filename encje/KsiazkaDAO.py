#!/usr/bin/python
# -*- coding: UTF-8 -*-
# from Encje import IRepozytoriumKsiazek
# from typing import List
#
# class KsiazkaDAO(IRepozytoriumKsiazek):
# 	def dodajKsiazke(self, aKsiazka : IKsiazka):
# 		pass
#
# 	def usunKsiazke(self, aIdKsiazki : int):
# 		pass
#
# 	def pobierzWszystkie(self) -> List:
# 		pass
#
# 	def AktualizujDane(self, aKsiazka : IKsiazka):
# 		pass
#
# 	def pobierzPoId(self, aId : int) -> IKsiazka:
# 		pass
#
# 	def aktualizujStan(self, aIdKsiazki : int, aNowyStan : int):
# 		pass


from typing import List
from encje.IRepozytoriumKsiazek import IRepozytoriumKsiazek
from encje.IKsiazka import IKsiazka
from encje.MagazynKsiazek import MagazynKsiazek

class KsiazkaDAO(IRepozytoriumKsiazek):
    def __init__(self):
        # Relacja z diagramu: DAO -> Magazyn
        self._magazyn = MagazynKsiazek()

    def dodajKsiazke(self, ksiazka: IKsiazka):
        print("DAO: Dodaję książkę do Magazynu...")
        self._magazyn.dodaj(ksiazka)

    def usunKsiazke(self, idKsiazki: int):
        self._magazyn.usun(idKsiazki)

    def pobierzWszystkie(self) -> List[IKsiazka]:
        return self._magazyn.pobierz_wszystkie()

    def AktualizujDane(self, ksiazka: IKsiazka):
        self._magazyn.aktualizuj(ksiazka)

    def pobierzPoId(self, id: int) -> IKsiazka:
        return self._magazyn.znajdz_po_id(id)

    def aktualizujStan(self, idKsiazki: int, nowyStan: int):
        # Logika: pobierz z magazynu -> zmień stan -> (magazyn trzyma referencję, więc się zaktualizuje)
        ksiazka = self._magazyn.znajdz_po_id(idKsiazki)
        if ksiazka:
            # Zakładamy, że obiekt IKsiazka ma pole stanMagazynowy
            # Jeśli IKsiazka to interfejs, upewnij się, że ta operacja jest tam dozwolona,
            # lub rzutuj na konkretną klasę Ksiazka
            if hasattr(ksiazka, 'stanMagazynowy'):
                 ksiazka.stanMagazynowy = nowyStan
            else:
                 print("Błąd: Obiekt nie ma pola stanMagazynowy")