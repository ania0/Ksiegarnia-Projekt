#!/usr/bin/python
# -*- coding: UTF-8 -*-
# from Encje import Uzytkownik
# from Encje import IRepozytoriumUzytkownika
# from typing import List
#
# class UzytkownikDAO(IRepozytoriumUzytkownika):
# 	def rejestrujUzytkownika(self, aUzytkownik : Class_Diagram___Class_in_a_Package__Airline_.Encje.Uzytkownik):
# 		pass
#
# 	def znajdzUzytkownikaPoEmail(self, aEmail : String) -> Uzytkownik:
# 		pass
#
# 	def czyIstnieje(self, aEmail : String) -> long:
# 		pass
#
# 	def usun(self, aIdUzytkownika : int):
# 		pass
#
# 	def pobierzDaneUzytkownika(self, aIdUzytkownika : int) -> Uzytkownik:
# 		pass
#



from encje.IRepozytoriumUzytkownika import IRepozytoriumUzytkownika
from encje.Uzytkownik import Uzytkownik
from encje.MagazynUzytkownikow import MagazynUzytkownikow
from typing import Optional


class UzytkownikDAO(IRepozytoriumUzytkownika):
    def __init__(self):
        self._magazyn = MagazynUzytkownikow()

    def rejestrujUzytkownika(self, uzytkownik: Uzytkownik):
        print(f"DAO: Zapisuję użytkownika {uzytkownik.login} do Magazynu...")
        self._magazyn.dodaj(uzytkownik)

    def znajdzUzytkownikaPoEmail(self, email: str) -> Optional[Uzytkownik]:
        wszyscy = self._magazyn.pobierz_wszystkich()

        for u in wszyscy:
            if u.login == email:
                return u
        return None

    def czyIstnieje(self, email: str) -> bool:
        uzytkownik = self.znajdzUzytkownikaPoEmail(email)
        return uzytkownik is not None

    def usun(self, login: str):
        print(f"DAO: Usuwam użytkownika {login} z Magazynu...")
        self._magazyn.usun_po_loginie(login)

    def pobierzDaneUzytkownika(self, login: str) -> Optional[Uzytkownik]:
        return self.znajdzUzytkownikaPoEmail(login)