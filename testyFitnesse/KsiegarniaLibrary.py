import sys
import os

# Automatyczne ustawienie sciezki - folder 'encie' i 'kontrola'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from encje.FasadaEncji import FasadaEncji
from encje.UzytkownikDAO import UzytkownikDAO
from encje.KsiazkaDAO import KsiazkaDAO
from encje.ZamowienieDAO import ZamowienieDAO
from encje.FabrykaKsiazek import FabrykaKsiazek
from encje.DekoratorRabatuLojalnosciowego import DekoratorRabatuLojalnosciowego
from kontrola.KsiegarniaKontrolaFacade import KsiegarniaKontrolaFacade
from encje.Klient import Klient
from encje.Administrator import Administrator


class KsiegarniaLibrary:
    def __init__(self):
        self.uzytkownik_dao = UzytkownikDAO()
        self.ksiazka_dao = KsiazkaDAO()
        self.zamowienie_dao = ZamowienieDAO()
        self.fabryka_ksiazek = FabrykaKsiazek()
        self.dekorator_rabatu = DekoratorRabatuLojalnosciowego

        self.encje_fasada = FasadaEncji(
            self.ksiazka_dao, self.uzytkownik_dao, self.zamowienie_dao,
            self.fabryka_ksiazek, self.dekorator_rabatu
        )
        self.kontrola_fasada = KsiegarniaKontrolaFacade(self.encje_fasada)

    def zarejestruj_uzytkownika(self, imie, nazwisko, email, haslo, adres, typ="klient"):
        try:
            if typ == "admin":
                u = Administrator(imie, nazwisko, email, haslo, id=None)
            else:
                u = Klient(imie, nazwisko, email, haslo, adres, False)
            self.encje_fasada.rejestrujUzytkownika(u)
            return "Sukces"
        except ValueError as e:
            return str(e)

    def zaloguj(self, typ, email, haslo):
        if typ.lower() == "klient":
            u = self.kontrola_fasada.zalogujKlienta(haslo, email)
        else:
            u = self.kontrola_fasada.zalogujAdministratora(haslo, email)
        return u is not None

    def dodaj_ksiazke(self, typ, tytul, autor, cena, isbn, gatunek, ilosc=10):
        try:
            sciezka = "file.pdf" if typ.lower() == "ebook" else ""
            k = self.fabryka_ksiazek.utworzKsiazke(
                typ, tytul, autor, float(cena), int(isbn), gatunek, int(ilosc), "Opis", sciezka
            )
            self.encje_fasada.dodajKsiazke(k)
            return "Sukces"
        except ValueError as e:
            return str(e)

    def usun_uzytkownika(self, email):
        u = self.encje_fasada.znajdzUzytkownikaPoEmailu(email)
        if u:
            self.encje_fasada.usun(u.id)
            return True
        return False

    def sprawdz_czy_uzytkownik_istnieje(self, email):
        return self.encje_fasada.czyIstnieje(email)

    def zmien_stan_magazynowy(self, isbn, nowy_stan):
        try:
            self.encje_fasada.aktualizujStan(int(isbn), int(nowy_stan))
            return "Sukces"
        except Exception as e:
            return str(e)

    def pobierz_cene_ksiazki(self, isbn):
        k = self.encje_fasada.pobierzPoISBN(int(isbn))
        return k.cena if k else 0