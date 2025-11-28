from encje.Uzytkownik import Uzytkownik
#dziedziczy po klasie uzytkownik

class Administrator(Uzytkownik):
    def __init__(self, imie: str, nazwisko: str, email: str, hashHasla: str, id: int) -> None:
        super().__init__(imie, nazwisko, email, hashHasla, id)

