from abc import ABC, abstractmethod


class IKsiazka(ABC):
    def __init__(self, tytul: str, autor: str, ISBN: int, gatunek: str, cena: float, opis: str):
        self.tytul: str = tytul
        self.autor: str = autor
        self.ISBN: int = ISBN
        self.gatunek: str = gatunek
        self.cena: float = cena
        self.opis: str = opis

    def pobierzCene(self) -> float:
        return self.cena

    def pobierzISBN(self) -> int:
        return self.ISBN

    @abstractmethod
    def ustawTytul(self, tytul: str) -> None:
        pass

    @abstractmethod
    def ustawAutora(self, autor: str) -> None:
        pass

    @abstractmethod
    def ustawGatunek(self, gatunek: str) -> None:
        pass

    @abstractmethod
    def ustawCene(self, cena: float) -> None:
        pass

    @abstractmethod
    def ustawOpis(self, opis: str) -> None:
        pass

