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

from typing import List # TU
from encje.IRepozytoriumUzytkownika import IRepozytoriumUzytkownika
from encje.Uzytkownik import Uzytkownik

class UzytkownikDAO(IRepozytoriumUzytkownika):

    def __init__(self):
        # referencja do magazynu (agregacja)
        self._magazyn = None  # w pełnej implementacji: MagazynUzytkownikow

    def rejestrujUzytkownika(self, uzytkownik: Uzytkownik) -> None:
        """Dodaje użytkownika do magazynu."""
        self._magazyn.append(uzytkownik)

    def znajdzUzytkownikaPoEmailu(self, email: str) -> Optional[Uzytkownik]:
        """Zwraca użytkownika o podanym emailu lub None jeśli nie istnieje."""
        for u in self._magazyn:
            if u.email == email:
                return u
        return None

    def czyIstnieje(self, email: str) -> bool:
        """Sprawdza, czy istnieje użytkownik o podanym emailu."""
        return any(u.email == email for u in self._magazyn)

    def usun(self, idUzytkownika: int) -> None:
        """Usuwa użytkownika o podanym ID."""
        self._magazyn = [u for u in self._magazyn if u.pobierzId() != idUzytkownika]

    def pobierzDaneUzytkownika(self, idUzytkownika: int) -> Optional[Uzytkownik]:
        """Zwraca użytkownika o podanym ID lub None jeśli nie istnieje."""
        for u in self._magazyn:
            if u.pobierzId() == idUzytkownika:
                return u
        return None