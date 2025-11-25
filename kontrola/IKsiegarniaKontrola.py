from abc import ABC, abstractmethod
from typing import List, Optional
from encje.Uzytkownik import Uzytkownik
from encje.KsiazkaPapierowa import KsiazkaPapierowa
from encje.Ebook import Ebook


class IKsiegarniaKontrola(ABC):

    @abstractmethod
    def stworzKonto(self, login: str, haslo: str, email: str) -> bool:
        """Tworzy nowe konto użytkownika."""
        pass

    @abstractmethod
    def zalogujKlienta(self, login: str, haslo: str) -> Optional[Uzytkownik]:
        """Zwraca obiekt użytkownika jeśli logowanie przebiegło pomyślnie."""
        pass

    @abstractmethod
    def zalogujAdministratora(self, login: str, haslo: str) -> Optional[Uzytkownik]:
        """Loguje administratora i zwraca jego encję."""
        pass



    @abstractmethod
    def przegladajKsiazki(self) -> List[Ksiazka]: #nie jestem pewna jak tu rozroznic ebook od ksiazki papier
        """Zwraca listę wszystkich książek w katalogu."""
        pass

    @abstractmethod
    def wybierzKsiazke(self, id_ksiazki: int) -> Optional[Ksiazka]:
        """Zwraca książkę o wskazanym ID."""
        pass

    @abstractmethod
    def zarzadzajKatalogiem(self, operacja: str, ksiazka: Optional[Ksiazka] = None) -> bool:
        """
        Pozwala administratorowi zarządzać katalogiem.
        operacja może być: 'dodaj', 'usun', 'aktualizuj'.
        """
        pass


    @abstractmethod
    def zlozZamowienie(self, id_klienta: int, lista_id_ksiazek: List[int]) -> bool:
        """Składa zamówienie dla danego klienta."""
        pass


    @abstractmethod
    def przegladajHistorie(self, id_klienta: int):
        """Zwraca historię zamówień klienta."""
        pass

    @abstractmethod
    def przegladajRaporty(self) -> List[str]:
        """Administrator przegląda raporty sprzedaży, aktywności itp."""
        pass


    @abstractmethod
    def usunKonto(self, id_klienta: int) -> bool:
        """Usuwa konto klienta o podanym ID."""
        pass

