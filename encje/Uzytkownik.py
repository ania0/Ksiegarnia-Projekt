from typing import Optional


class Uzytkownik:
    def weryfikujHaslo(self, podaneHaslo: str) -> bool:
        pass

    def pobierzId(self) -> int:
        pass

    def __init__(self, imie: str,
                 nazwisko: str,
                 email: str,
                 hashHasla: Optional[str] = None,
                 id: Optional[int] = None):
        self.imie: str = imie
        self.nazwisko: str = nazwisko
        self.hashHasla: Optional[str] = hashHasla
        self.email: str = email
        self.id: Optional[int] = id

    def weryfikujHaslo(self, podaneHaslo: str) -> bool:
        raise NotImplementedError("weryfikujHaslo() nie jest jeszcze zaimplementowane.")

    def pobierzId(self) -> Optional[int]:
        return self._id