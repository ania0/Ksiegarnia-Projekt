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

from encje.Uzytkownik import Uzytkownik
from encje.Zamowienie import Zamowienie
from encje.Klient import Klient
from encje.IKsiazka import IKsiazka
from typing import List

from encje.IRepozytoriumKsiazek import IRepozytoriumKsiazek
from encje.IRepozytoriumUzytkownika import IRepozytoriumUzytkownika
from encje.IRepozytoriumZamowien import IRepozytoriumZamowien
from encje.IEncjeFasada import IEncjeFasada
from encje.FabrykaKsiazek import FabrykaKsiazek
from encje.DekoratorRabatuLojalnosciowego import DekoratorRabatuLojalnosciowego
from encje.ICena import ICena

# posrednik miedzy kodem biznesowym a repo
class FasadaEncji:
    def __init__(self, repoKsiazek: IRepozytoriumKsiazek,
                 repoUzytkownika: IRepozytoriumUzytkownika,
                 repoZamowien: IRepozytoriumZamowien,
                 fabrykaKsiazek: FabrykaKsiazek):
        self.repoKsiazek = repoKsiazek
        self.repoUzytkownika = repoUzytkownika
        self.repoZamowien = repoZamowien
        self.fabrykaKsiazek = fabrykaKsiazek

#deleguje zadania do repo i ukrywa szczegoly
    # Uzytkownicy
    def rejestrujUzytkownika(self, uzytkownik):
        self.repoUzytkownika.rejestrujUzytkownika(uzytkownik)

    def znajdzUzytkownikaPoEmail(self, email: str) -> Uzytkownik:
        return self.repoUzytkownika.znajdzUzytkownikaPoEmail(email)

    def czyIstnieje(self, email: str) -> bool:
        return self.repoUzytkownika.czyIstnieje(email)

    def usun(self, idUzytkownika: int):
        self.repoUzytkownika.usun(idUzytkownika)

    def pobierzDaneUzytkownika(self, idUzytkownika: int) -> Uzytkownik:
        return self.repoUzytkownika.pobierzDaneUzytkownika(idUzytkownika)

    # Ksiazki
    # metoda moze przyjmować obiekt implementujący ten interfejs
    def dodajKsiazke(self, ksiazka: IKsiazka):
        self.repoKsiazek.dodajKsiazke(ksiazka)

    def usunKsiazke(self, idKsiazki: int):
        self.repoKsiazek.usunKsiazke(idKsiazki)

    def pobierzWszystkie(self) -> List[IKsiazka]:
        return self.repoKsiazek.pobierzWszystkie()

    def AktualizujDane(self, ksiazka: IKsiazka):
        self.repoKsiazek.AktualizujDane(ksiazka)

    def pobierzPoId(self, id: int) -> IKsiazka:
        return self.repoKsiazek.pobierzPoId(id)

    def aktualizujStan(self, idKsiazki: int, nowyStan: int):
        self.repoKsiazek.aktualizuj(idKsiazki, nowyStan)

    # Zamowienia
    def zapiszZamowienie(self, zamowienie: Zamowienie):
        self.repoZamowien.zapiszZamowienie(zamowienie)

    def pobierzHistorieDlaKlienta(self, idKlienta: int) -> List[Zamowienie]:
        return self.repoZamowien.pobierzHistorieDlaKlienta(idKlienta)

    def pobierzWszystkieZamowienia(self) -> List[Zamowienie]:
        return self.repoZamowien.pobierzWszystkieZamowienia()

# wzorzec dekoratora
    # zamowienie implementuje interfejs ICena
    # jesli klient lojalny – owijamy zamowienie dekoratorem rabatu
    def obliczCeneOstateczna(self, zamowienie: Zamowienie, klient: Klient) -> float:
        komponent_ceny: ICena = zamowienie
        if klient.klientLojalny:
            # dodawanie funkcji bez zmieniania podstawowej klasy
            komponent_ceny = DekoratorRabatuLojalnosciowego(komponent_ceny)
        return komponent_ceny.obliczCene()
