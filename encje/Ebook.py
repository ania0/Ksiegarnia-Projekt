from encje.IKsiazka import IKsiazka


class Ebook(IKsiazka):
    def __init__(self, tytul: str, autor: str, ISBN: int, gatunek: str,
                 cena: float, sciezkaDoPliku: str, opis: str):
        super().__init__(tytul, autor, ISBN, gatunek, cena, opis)
        self.sciezkaDoPliku: str = sciezkaDoPliku

    # Ponieważ dziedziczymy, implementacja jest identyczna jak w papierowej dla pól wspólnych,
    # ale musi być obecna, bo metody w IKsiazka są abstrakcyjne.

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