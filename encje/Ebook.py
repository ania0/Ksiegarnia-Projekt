from encje.IKsiazka import IKsiazka  # import interf książki, po którym dziedziczy Ebook


# kl implementująca interf IKsiazka
class Ebook(IKsiazka):

    # konstruktor Ebook
    def __init__(self, tytul: str, autor: str, ISBN: int, gatunek: str,
                 cena: float, sciezkaDoPliku: str, opis: str):
        self.tytul: str = tytul
        self.autor: str = autor
        self.ISBN: int = ISBN
        self.gatunek: str = gatunek
        self.cena: float = cena
        self.sciezkaDoPliku: str = sciezkaDoPliku
        self.opis: str = opis


    # implementacja met z interf IKsiazka - zwraca cenę e-booka - NA DIAGRAMIE JUZ JEJ NIE MA
    def pobierzCene(self) -> float:
        """
            Tymczasowa implementacja – sygnatura operacji.
            Zwraca testową wartość lub podnosi wyjątek.
            """
        raise NotImplementedError("pobierzCene() nie jest jeszcze zaimplementowane.")

