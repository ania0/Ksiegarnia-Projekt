# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
# from typing import List
#
# class Uzytkownik(object):
# 	def __init__(self):
# 		self.___imie : String = None
# 		self.___nazwisko : String = None
# 		self.___hashHasla : String = None
# 		self.___email : String = None
# 		self._unnamed_Zamowienie_ = []
# 		"""# @AssociationMultiplicity *"""
#


class Uzytkownik:
    """Encja użytkownika"""

    def __init__(self, imie=None, nazwisko=None, hashHasla=None, email=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.hashHasla = hashHasla
        self.email = email
