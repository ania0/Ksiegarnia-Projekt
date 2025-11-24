# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
# from Encje import Uzytkownik
# from typing import List
#
# class Klient(Uzytkownik):
# 	def aktualizujStatus(self):
# 		pass
#
# 	def __init__(self):
# 		self.___adresWysylki : String = None
# 		self.___klinetLojalny : long = None
#


from encje.Uzytkownik import Uzytkownik

#dziedziczy po klasie uzytkownik
class Klient(Uzytkownik):
    def __init__(self, imie: str, nazwisko: str, email: str, hashHasla: str,
                 adresWysylki: str, klientLojalny: bool):
        # konstruktor klasy Uzytkownik
        super().__init__(imie, nazwisko, email, hashHasla)
        self.adresWysylki: str = adresWysylki
        self.klientLojalny: bool = klientLojalny

    def aktualizujStatus(self):
        pass
