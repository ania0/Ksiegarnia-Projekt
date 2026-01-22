from typing import List, Optional  # TU
from encje.IRepozytoriumUzytkownika import IRepozytoriumUzytkownika
from encje.Uzytkownik import Uzytkownik

class UzytkownikDAO(IRepozytoriumUzytkownika):

    def __init__(self):
        # referencja do magazynu (agregacja)
        self._magazyn: List[Uzytkownik] = []

    def rejestrujUzytkownika(self, uzytkownik: Uzytkownik) -> None:
        """Dodaje użytkownika do magazynu."""
        self._magazyn.append(uzytkownik)
        uzytkownik.id = len(self._magazyn)

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

    def aktualizujDaneUzytkownika(
            self,
            uzytkownik: Uzytkownik,
            noweImie: Optional[str] = None,
            noweNazwisko: Optional[str] = None,
            nowyEmail: Optional[str] = None,
            noweHaslo: Optional[str] = None,
            nowyAdres: Optional[str] = None
    ) -> None:
        pass

    def pobierzWszystkich(self) -> List[Uzytkownik]:
        return self._magazyn