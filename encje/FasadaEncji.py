#!/usr/bin/python
# -*- coding: UTF-8 -*-
# from Encje import Uzytkownik
# from Encje import Zamowienie
# from Encje import Klient
# import IEncjeFasada
# from typing import List
#
# class Fasada_encji(IEncjeFasada):
# 	def rejestrujUzytkownika(self, aUzytkownik : Class_Diagram___Class_in_a_Package__Airline_.Encje.Uzytkownik):
# 		pass
#
# 	def znajdzUzytkownikaPoEmail(self, aEmail : String) -> Uzytkownik:
# 		pass
#
# 	def czyIstnieje(self, aEmail : String) -> long:
# 		pass
#
# 	def usun(self, aIduzytkownika : int):
# 		pass
#
# 	def pobierzDaneUzytkownika(self, aIdUzytkownika : int) -> Uzytkownik:
# 		pass
#
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
#
# 	def zapiszZamowienie(self, aZamowienie : Zamowienie):
# 		pass
#
# 	def pobierzHistorieDlaKlienta(self, aIdKlienta : int) -> List:
# 		pass
#
# 	def pobierzWszystkieZamowienia(self) -> List:
# 		pass
#
# 	def obliczCeneOstateczna(self, aZamowienie : Zamowienie, aKlient : Klient) -> float:
# 		pass
#


from encje.IRepozytoriumKsiazek import IRepozytoriumKsiazek
from encje.IRepozytoriumUzytkownika import IRepozytoriumUzytkownika
from encje.IRepozytoriumZamowien import IRepozytoriumZamowien
from encje.IEncjeFasada import IEncjeFasada
class FasadaEncji:
    def __init__(self, repoKsiazek: IRepozytoriumKsiazek,
                 repoUzytkownika: IRepozytoriumUzytkownika,
                 repoZamowien: IRepozytoriumZamowien):
        self.repoKsiazek = repoKsiazek
        self.repoUzytkownika = repoUzytkownika
        self.repoZamowien = repoZamowien

    # Uzytkownicy
    def rejestrujUzytkownika(self, uzytkownik):
        pass

    def znajdzUzytkownikaPoEmail(self, email: str):
        pass

    def czyIstnieje(self, email: str) -> bool:
        pass

    def usun(self, idUzytkownika: int):
        pass

    def pobierzDaneUzytkownika(self, idUzytkownika: int):
        pass

    # Ksiazki
    def dodajKsiazke(self, ksiazka):
        pass

    def usunKsiazke(self, idKsiazki: int):
        pass

    def pobierzWszystkie(self):
        pass

    def AktualizujDane(self, ksiazka):
        pass

    def pobierzPoId(self, id: int):
        pass

    def aktualizujStan(self, idKsiazki: int, nowyStan: int):
        pass

    # Zamowienia
    def zapiszZamowienie(self, zamowienie):
        pass

    def pobierzHistorieDlaKlienta(self, idKlienta: int):
        pass

    def pobierzWszystkieZamowienia(self):
        pass

    def obliczCeneOstateczna(self, zamowienie, klient):
        pass
