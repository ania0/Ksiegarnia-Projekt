

class Uzytkownik:
    def weryfikujHaslo(self, podaneHaslo: str) -> bool:
        pass

    def pobierzId(self) -> int:
        pass

    def __init__(self, imie=str, nazwisko=str, hashHasla=str, email=str, id = None):
        self.imie: str = imie
        self.nazwisko: str = nazwisko
        self.hashHasla: str = hashHasla
        self.email: str = email
        self.id = id
