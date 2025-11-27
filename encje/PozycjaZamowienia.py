from encje.IKsiazka import IKsiazka

class PozycjaZamowienia:
    def __init__(self, ksiazka: IKsiazka, ilosc: int, cenaJednostkowa: float):
        self.ksiazka: IKsiazka = ksiazka
        self.ilosc: int = ilosc
        self.cenaJednostkowa: float = cenaJednostkowa

