# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
# from abc import ABCMeta, abstractmethod
# from Encje import Uzytkownik
# from Encje import Zamowienie
# from Encje import Klient
# from typing import List
#
# class IEncjeFasada(object):
# 	"""@Interface"""
# 	__metaclass__ = ABCMeta
# 	@abstractmethod
# 	def rejestrujUzytkownika(self, aUzytkownik : Class_Diagram___Class_in_a_Package__Airline_.Encje.Uzytkownik):
# 		pass
#
# 	@abstractmethod
# 	def znajdzUzytkownikaPoEmail(self, aEmail : String) -> Uzytkownik:
# 		pass
#
# 	@abstractmethod
# 	def czyIstnieje(self, aEmail : String) -> long:
# 		pass
#
# 	@abstractmethod
# 	def usun(self, aIduzytkownika : int):
# 		pass
#
# 	@abstractmethod
# 	def pobierzDaneUzytkownika(self, aIdUzytkownika : int) -> Uzytkownik:
# 		pass
#
# 	@abstractmethod
# 	def dodajKsiazke(self, aKsiazka : IKsiazka):
# 		pass
#
# 	@abstractmethod
# 	def usunKsiazke(self, aIdKsiazki : int):
# 		pass
#
# 	@abstractmethod
# 	def pobierzWszystkie(self) -> List:
# 		pass
#
# 	@abstractmethod
# 	def AktualizujDane(self, aKsiazka : IKsiazka):
# 		pass
#
# 	@abstractmethod
# 	def pobierzPoId(self, aId : int) -> IKsiazka:
# 		pass
#
# 	@abstractmethod
# 	def aktualizujStan(self, aIdKsiazki : int, aNowyStan : int):
# 		pass
#
# 	@abstractmethod
# 	def zapiszZamowienie(self, aZamowienie : Zamowienie):
# 		pass
#
# 	@abstractmethod
# 	def pobierzHistorieDlaKlienta(self, aIdKlienta : int) -> List:
# 		pass
#
# 	@abstractmethod
# 	def pobierzWszystkieZamowienia(self) -> List:
# 		pass
#
# 	@abstractmethod
# 	def obliczCeneOstateczna(self, aZamowienie : Zamowienie, aKlient : Klient) -> float:
# 		pass
#
#

# -*- coding: UTF-8 -*-
from abc import ABC, abstractmethod
from typing import List
from encje.Uzytkownik import Uzytkownik
from encje.Klient import Klient
from encje.Zamowienie import Zamowienie
from encje.IKsiazka import IKsiazka

class IEncjeFasada(ABC):
    """Interface dla fasady operacji na encjach"""

    # --- Użytkownicy ---
    @abstractmethod
    def rejestrujUzytkownika(self, uzytkownik: Uzytkownik):
        pass

    @abstractmethod
    def znajdzUzytkownikaPoEmail(self, email: str) -> Uzytkownik:
        pass

    @abstractmethod
    def czyIstnieje(self, email: str) -> bool:
        pass

    @abstractmethod
    def usun(self, idUzytkownika: int):
        pass

    @abstractmethod
    def pobierzDaneUzytkownika(self, idUzytkownika: int) -> Uzytkownik:
        pass

    # --- Książki ---
    @abstractmethod
    def dodajKsiazke(self, ksiazka: IKsiazka):
        pass

    @abstractmethod
    def usunKsiazke(self, idKsiazki: int):
        pass

    @abstractmethod
    def pobierzWszystkie(self) -> List[IKsiazka]:
        pass

    @abstractmethod
    def aktualizujDane(self, ksiazka: IKsiazka):
        pass

    @abstractmethod
    def pobierzPoId(self, id: int) -> IKsiazka:
        pass

    @abstractmethod
    def aktualizujStan(self, idKsiazki: int, nowyStan: int):
        pass

    # --- Zamówienia ---
    @abstractmethod
    def zapiszZamowienie(self, zamowienie: Zamowienie):
        pass

    @abstractmethod
    def pobierzHistorieDlaKlienta(self, idKlienta: int) -> List[Zamowienie]:
        pass

    @abstractmethod
    def pobierzWszystkieZamowienia(self) -> List[Zamowienie]:
        pass

    @abstractmethod
    def obliczCeneOstateczna(self, zamowienie: Zamowienie, klient: Klient) -> float:
        pass
