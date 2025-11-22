from typing import List, Optional
from encje.Uzytkownik import Uzytkownik

class MagazynUzytkownikow:
    """
    Symulacja tabeli użytkowników w bazie danych.
    """
    def __init__(self):
        # To jest jedyne miejsce w systemie, gdzie dane są przechowywane w pamięci
        self._tabela_uzytkownikow: List[Uzytkownik] = []

    def dodaj(self, uzytkownik: Uzytkownik):
        self._tabela_uzytkownikow.append(uzytkownik)

    def pobierz_wszystkich(self) -> List[Uzytkownik]:
        return self._tabela_uzytkownikow

    def usun_po_id(self, id_uzytkownika: int):
        # Filtrujemy listę, usuwając użytkownika o podanym ID
        # Używamy getattr, aby uniknąć błędu, jeśli obiekt nie ma jeszcze nadanego ID
        self._tabela_uzytkownikow = [
            u for u in self._tabela_uzytkownikow
            if getattr(u, 'id', None) != id_uzytkownika
        ]