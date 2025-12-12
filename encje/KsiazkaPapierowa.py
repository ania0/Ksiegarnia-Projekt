from encje.IKsiazka import IKsiazka

class KsiazkaPapierowa(IKsiazka):
    def __init__(self, tytul: str, autor: str, ISBN: int, gatunek: str,
                 cena: float, stanMagazynowy: int, opis: str):
        super().__init__(tytul, autor, ISBN, gatunek, cena, opis)
        self.stanMagazynowy: int = stanMagazynowy

    def ustawTytul(self, tytul: str) -> None:
        self.tytul = tytul

    def ustawAutora(self, autor: str) -> None:
        self.autor = autor

    def ustawGatunek(self, gatunek: str) -> None:
        self.gatunek = gatunek

    def ustawCene(self, cena: float) -> None:
        self.cena = cena

    def ustawOpis(self, opis: str) -> None:
        self.opis = opis