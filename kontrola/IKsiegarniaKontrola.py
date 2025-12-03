from abc import ABC, abstractmethod, abstractproperty
from typing import List, Optional
from encje.Uzytkownik import Uzytkownik
from encje.KsiazkaPapierowa import KsiazkaPapierowa
from encje.Ebook import Ebook
from encje.Uzytkownik import Uzytkownik


class IKsiegarniaKontrola(ABC):

    @abstractmethod
    def stworzKonto(self, haslo: str, email: str) -> None:
        """Tworzy nowe konto użytkownika."""
        pass

    @abstractmethod
    def zalogujKlienta(self, haslo: str, email: str) -> None:
        """Zwraca obiekt użytkownika jeśli logowanie przebiegło pomyślnie."""
        pass

    @abstractmethod
    def zalogujAdministratora(self, haslo : str, email : str) -> None:
        """Loguje administratora i zwraca jego encję."""
        pass

    @abstractmethod
    def przegladajKsiazki(self) -> None:
        """Zwraca listę wszystkich książek w katalogu."""
        pass

    @abstractmethod
    def wybierzKsiazke(self, ISBN: int) -> None:
        """Zwraca książkę o wskazanym ID."""
        pass

    @abstractmethod
    def zarzadzajKatalogiem(self) -> None:
        """
        Pozwala administratorowi zarządzać katalogiem.
        operacja może być: 'dodaj', 'usun', 'aktualizuj'.
        """
        pass

    @abstractmethod
    def przegladajHistorie(self, id_klienta: int) -> None:
        """Zwraca historię zamówień klienta."""
        pass

    @abstractmethod
    def przegladajRaporty(self) -> None:
        """Administrator przegląda raporty sprzedaży, aktywności itp."""
        pass


    @abstractmethod
    def usunKonto(self, id_klienta: int) -> None:
        """Usuwa konto klienta o podanym ID."""
        pass

