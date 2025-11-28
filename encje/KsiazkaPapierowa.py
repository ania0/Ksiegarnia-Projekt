from encje.IKsiazka import IKsiazka

# dziedziczy po IKsiazka
class KsiazkaPapierowa(IKsiazka):
    def __init__(self, tytul: str, autor: str, ISBN: int, gatunek: str,
                 cena: float, stanMagazynowy: int, opis: str):
        self.tytul: str = tytul
        self.autor: str = autor
        self.ISBN: int = ISBN
        self.gatunek: str = gatunek
        self.cena: float = cena
        self.stanMagazynowy: int = stanMagazynowy
        self.opis: str = opis

    def pobierzCene(self) -> float:
        return self.cena
