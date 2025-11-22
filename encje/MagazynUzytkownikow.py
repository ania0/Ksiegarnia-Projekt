from encje.Uzytkownik import Uzytkownik

class MagazynUzytkownikow:

    def __init__(self):
        # To jest Twoja "tabela" w bazie danych
        self._lista_uzytkownikow = []

    def dodaj(self, uzytkownik: Uzytkownik):
        self._lista_uzytkownikow.append(uzytkownik)

    def pobierz_wszystkich(self):
        return self._lista_uzytkownikow

    def usun_po_loginie(self, login: str):
        self._lista_uzytkownikow = [u for u in self._lista_uzytkownikow if u.login != login]