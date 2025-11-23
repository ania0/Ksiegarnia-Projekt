from abc import ABC, abstractmethod


class IKsiegarniaKontrola(ABC):
    @abstractmethod
    def stworzKonto(self, dane): pass

    @abstractmethod
    def zalogujKlienta(self, login, haslo): pass

    @abstractmethod
    def zarzadzajKatalogiem(self, polecenie): pass

    @abstractmethod
    def zlozZamowienie(self, koszyk): pass

    @abstractmethod
    def zalogujAdministratora(self, login, haslo): pass

    @abstractmethod
    def przegladajRaporty(self): pass

    @abstractmethod
    def usunKonto(self): pass

    @abstractmethod
    def przegladajKsiazki(self): pass

    @abstractmethod
    def wybierzKsiazke(self, id): pass

    @abstractmethod
    def przegladajHistorie(self): pass