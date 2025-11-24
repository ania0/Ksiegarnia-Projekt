from encje.Uzytkownik import Uzytkownik

#dziedziczy po klasie uzytkownik
class Klient(Uzytkownik):
    def __init__(self, imie: str, nazwisko: str, email: str, hashHasla: str,
                 adresWysylki: str, klientLojalny: bool):
        # konstruktor klasy Uzytkownik
        super().__init__(imie, nazwisko, email, hashHasla)
        self.adresWysylki: str = adresWysylki
        self.klientLojalny: bool = klientLojalny

    def aktualizujStatus(self):
        pass
