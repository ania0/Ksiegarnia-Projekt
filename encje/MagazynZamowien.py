from encje.Zamowienie import Zamowienie 

class MagazynZamowien:
    def __init__(self):
        self._zamowienia = []

    def dodaj(self, zamowienie: Zamowienie):
        self._zamowienia.append(zamowienie)

    def pobierz_wszystkie(self):
        return self._zamowienia

    def pobierz_dla_klienta(self, id_klienta: int):
        return [z for z in self._zamowienia if getattr(z.uzytkownik, 'id', None) == id_klienta]