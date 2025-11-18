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
from typing import List

class UzytkownikDAO(IRepozytoriumUzytkownika):
    def __init__(self):
        self.uzytkownicy: List[Uzytkownik] = []

    def rejestrujUzytkownika(self, uzytkownik: Uzytkownik):
        self.uzytkownicy.append(uzytkownik)

    def znajdzUzytkownikaPoEmail(self, email: str) -> Uzytkownik:
        for u in self.uzytkownicy:
            if u.email == email:
                return u
        return None

    def czyIstnieje(self, email: str) -> bool:
        return any(u.email == email for u in self.uzytkownicy)

    def usun(self, idUzytkownika: int):
        self.uzytkownicy = [u for u in self.uzytkownicy if getattr(u, 'id', None) != idUzytkownika]

    def pobierzDaneUzytkownika(self, idUzytkownika: int) -> Uzytkownik:
        for u in self.uzytkownicy:
            if getattr(u, 'id', None) == idUzytkownika:
                return u
        return None
