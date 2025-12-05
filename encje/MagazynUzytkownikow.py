

from typing import List, Optional
from encje.Uzytkownik import Uzytkownik

class MagazynUzytkownikow:
    """
    Magazyn użytkowników – prosty magazyn w pamięci do testów.
    """

    def __init__(self):
        # Lista przechowująca użytkowników
        self._listaUzytkownikow: List[Uzytkownik] = []

    def pobierzListeUzytkownikow(self) -> List[Uzytkownik]:
        # Zwraca kopię listy, aby nie pozwolić na bezpośrednią modyfikację
        return self._listaUzytkownikow.copy()

    def dodaj(self, uzytkownik: Uzytkownik) -> None:
        self._listaUzytkownikow.append(uzytkownik)

    def usun(self, id: int) -> None:
        self._listaUzytkownikow = [
            u for u in self._listaUzytkownikow if u.id != id
        ]

    def pobierz(self, id: int) -> Optional[Uzytkownik]:
        for u in self._listaUzytkownikow:
            if u.id == id:
                return u
        return None

