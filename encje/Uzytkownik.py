from typing import Optional


class Uzytkownik:

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
        # Można tu zrobić prostą testową weryfikację np. porównanie hashów
        if self.hashHasla is None:
            return False
        return podaneHaslo == self.hashHasla  # testowa wersja

    def pobierzId(self) -> Optional[int]:
        return self.id

    def pobierzEmail(self) -> Optional[str]:
        return self.email