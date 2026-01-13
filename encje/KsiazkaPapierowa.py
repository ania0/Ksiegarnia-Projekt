from encje.IKsiazka import IKsiazka

class KsiazkaPapierowa(IKsiazka):
    def __init__(self, tytul: str, autor: str, ISBN: int, gatunek: str,
                 cena: float, stanMagazynowy: int, opis: str):
        self._waliduj_niepuste(tytul=tytul,
                               autor=autor,
                               gatunek=gatunek,
                               # stanMagazynowy=stanMagazynowy,
                               opis=opis)
        self._waliduj_formaty(tytul, autor, ISBN)

        super().__init__(tytul, autor, ISBN, gatunek, cena, opis)
        self.stanMagazynowy: int = stanMagazynowy

    def _waliduj_niepuste(self, **pola):
        for nazwa, wartosc in pola.items():
            if not str(wartosc).strip():
                raise ValueError(f"Pole '{nazwa}' nie może być puste!")

    def _waliduj_formaty(self, tytul, autor, ISBN):
        if not isinstance(ISBN, int) or len(str(ISBN)) != 13:
            raise ValueError("ISBN musi mieć dokładnie 13 cyfr.")

        if not tytul[0].isupper():
            raise ValueError("Tytuł musi zaczynać się z wielkiej litery.")

        czlony = autor.replace('-', ' ').split()
        for czlon in czlony:
            if not czlon[0].isupper():
                raise ValueError(f"Każdy człon nazwy autora musi zaczynać się wielką literą.")

    def ustawTytul(self, tytul: str) -> None:
        if not tytul.strip():
            raise ValueError("Tytuł nie może być pusty!")
        elif not tytul[0].isupper():
            raise ValueError("Tytuł musi zaczynać się z wielkiej litery.")
        self.tytul = tytul

    def ustawAutora(self, autor: str) -> None:
        czlony = autor.replace('-', ' ').split()
        if not czlony:
            raise ValueError("Pole autor nie może być puste.")
        for czlon in czlony:
            if not czlon[0].isupper():
                raise ValueError(f"Każdy człon autora musi zaczynać się wielką literą.")
        self.autor = autor

    def ustawGatunek(self, gatunek: str) -> None:
        if not gatunek.strip():
            raise ValueError("Gatunek nie może być pusty!")
        self.gatunek = gatunek

    def ustawCene(self, cena: float) -> None:
        self.cena = cena

    def ustawOpis(self, opis: str) -> None:
        if not opis.strip():
            raise ValueError("Opis nie może być pusty!")
        self.opis = opis