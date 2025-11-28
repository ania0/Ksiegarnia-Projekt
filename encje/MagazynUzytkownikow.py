from typing import List, Optional
from encje.Uzytkownik import Uzytkownik
from encje.IRepozytoriumUzytkownika import IRepozytoriumUzytkownika
from typing import List

# class MagazynUzytkownikow:
#     """
#     Symulacja tabeli użytkowników w bazie danych.
#     """
#     def __init__(self):
#         # To jest jedyne miejsce w systemie, gdzie dane są przechowywane w pamięci
#         self._tabela_uzytkownikow: List[Uzytkownik] = []
#
#     def dodaj(self, uzytkownik: Uzytkownik):
#         self._tabela_uzytkownikow.append(uzytkownik)
#
#     def pobierz_wszystkich(self) -> List[Uzytkownik]:
#         return self._tabela_uzytkownikow
#
#     def usun_po_id(self, id_uzytkownika: int):
#         # Filtrujemy listę, usuwając użytkownika o podanym ID
#         # Używamy getattr, aby uniknąć błędu, jeśli obiekt nie ma jeszcze nadanego ID
#         self._tabela_uzytkownikow = [
#             u for u in self._tabela_uzytkownikow
#             if getattr(u, 'id', None) != id_uzytkownika
#         ]


from typing import List
from encje.Uzytkownik import Uzytkownik

class MagazynUzytkownikow:

    def __init__(self):
        # lista przechowująca użytkowników
        self._listaUzytkownikow: List[Uzytkownik] = []
        """# @AssociationKind Aggregation"""

    # metody pomocnicze
    def pobierzListeUzytkownikow(self) -> List[Uzytkownik]:
        # return self._listaUzytkownikow
        raise NotImplementedError("pobierzUzytkownikow - niezaimplementowane.")

    def dodaj(self, uzytkownik: Uzytkownik) -> None:
        raise NotImplementedError("dodaj - niezaimplementowane.")

    def usun(self, id: int) -> None:
        raise NotImplementedError("usun - niezaimplementowane.")

    def pobierz(self, id: int) -> Uzytkownik:
        return None

    # metody z interfejsu IRepozytoriumUzytkownika
#    def rejestrujUzytkownika(self, uzytkownik: Uzytkownik) -> None:
#       raise NotImplementedError("rejestrujUzytkownika - niezaimplementowane.")
#
#    def znajdzUzytkownikaPoEmailu(self, email: str) -> Uzytkownik:
#        return None
#
#    def czyIstnieje(self, email: str) -> bool:
#        return False
#
#    def pobierzDaneUzytkownika(self, idUzytkownika: int) -> Uzytkownik:
#        return None
