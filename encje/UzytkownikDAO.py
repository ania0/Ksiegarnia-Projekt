# from encje.IRepozytoriumUzytkownika import IRepozytoriumUzytkownika
# from encje.Uzytkownik import Uzytkownik
# from encje.MagazynUzytkownikow import MagazynUzytkownikow
# from typing import Optional
#
# # wzorzec, oddzielić logikę dostępu do bazy danych od logiki aplikacji
#
#
# class UzytkownikDAO(IRepozytoriumUzytkownika):
#     def __init__(self):
#         self._magazyn = MagazynUzytkownikow()
#
#     def rejestrujUzytkownika(self, uzytkownik: Uzytkownik):
#         print(f"DAO: Zapisuję użytkownika {uzytkownik.login} do Magazynu...")
#         self._magazyn.dodaj(uzytkownik)
#
#     def znajdzUzytkownikaPoEmail(self, email: str) -> Optional[Uzytkownik]:
#         wszyscy = self._magazyn.pobierz_wszystkich()
#
#         for u in wszyscy:
#             if u.login == email:
#                 return u
#         return None
#
#     def czyIstnieje(self, email: str) -> bool:
#         uzytkownik = self.znajdzUzytkownikaPoEmail(email)
#         return uzytkownik is not None
#
#     def usun(self, idUzytkownika: int):
#         print(f"DAO: Usuwam użytkownika z Magazynu...")
#         self._magazyn.usun_po_id(idUzytkownika)
#
#     def pobierzDaneUzytkownika(self, login: str) -> Optional[Uzytkownik]:
#         return self.znajdzUzytkownikaPoEmail(login)

from typing import List
from encje.IRepozytoriumUzytkownika import IRepozytoriumUzytkownika
from encje.Uzytkownik import Uzytkownik

class UzytkownikDAO(IRepozytoriumUzytkownika):

    def __init__(self):
        # referencja do magazynu (agregacja)
        self._magazyn = None  # w pełnej implementacji: MagazynUzytkownikow

    def rejestrujUzytkownika(self, uzytkownik: Uzytkownik):
        raise NotImplementedError("rejestrujUzytkownika - niezaimplementowane.")

    def znajdzUzytkownikaPoEmailu(self, email: str) -> Uzytkownik:
        return None  # domyślna wartość

    def czyIstnieje(self, email: str) -> bool:
        return False  # domyślna wartość

    def usun(self, idUzytkownika: int):
        raise NotImplementedError("usun - niezaimplementowane.")

    def pobierzDaneUzytkownika(self, idUzytkownika: str) -> Uzytkownik:
        return None  # domyślna wartość
