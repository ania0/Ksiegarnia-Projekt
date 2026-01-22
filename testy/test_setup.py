# from encje.FasadaEncji import FasadaEncji
# from encje.Klient import Klient
# from encje.IRepozytoriumUzytkownika import IRepozytoriumUzytkownika
# from encje.IRepozytoriumKsiazek import IRepozytoriumKsiazek
# from encje.IRepozytoriumZamowien import IRepozytoriumZamowien
# from encje.FabrykaKsiazek import FabrykaKsiazek
# from encje.DekoratorRabatuLojalnosciowego import DekoratorRabatuLojalnosciowego
# from kontrola.KsiegarniaKontrolaFacade import KsiegarniaKontrolaFacade
#
# def przygotuj_system():
#     # Tu tworzymy repozytoria „mockowe” lub prawdziwe
#     repo_ksiazek = IRepozytoriumKsiazek()
#     repo_uzytkownikow = IRepozytoriumUzytkownika()
#     repo_zamowien = IRepozytoriumZamowien()
#     fabryka = FabrykaKsiazek()
#     dekorator = DekoratorRabatuLojalnosciowego()
#
#     encje = FasadaEncji(
#         repo_ksiazek,
#         repo_uzytkownikow,
#         repo_zamowien,
#         fabryka,
#         dekorator
#     )
#
#     # Tworzymy przykładowego klienta w systemie
#     klient = Klient("Jan", "Kowalski", "jan@test.pl", "haslo", "Testowa 1", False)
#     encje.rejestrujUzytkownika(klient)
#
#     # Kontrola
#     kontrola = KsiegarniaKontrolaFacade(encje)
#
#     # Możemy zwrócić jeszcze pustą listę książek lub zamówień jeśli potrzeba
#     return encje, kontrola, klient, None
# test_setup.py
from encje.FasadaEncji import FasadaEncji
from encje.Klient import Klient
from encje.FabrykaKsiazek import FabrykaKsiazek
from encje.DekoratorRabatuLojalnosciowego import DekoratorRabatuLojalnosciowego
from encje.MagazynZamowien import MagazynZamowien
from encje.MagazynUzytkownikow import MagazynUzytkownikow
from encje.MagazynKsiazek import MagazynKsiazek

class RepozytoriumKsiazek:
    """Adapter magazynu książek do FasadyEncji"""
    def __init__(self):
        self.magazyn = MagazynKsiazek()

    def dodajKsiazke(self, ksiazka):
        self.magazyn.dodaj(ksiazka)

    def usunKsiazke(self, ISBN):
        self.magazyn.usun(ISBN)

    def pobierzPoISBN(self, ISBN):
        return self.magazyn.pobierz(ISBN)

    def pobierzWszystkie(self):
        return self.magazyn.pobierzListeKsiazek()

    def aktualizujDane(self, ksiazka):
        # dla uproszczenia nadpisujemy książkę o tym samym ISBN
        existing = self.magazyn.pobierz(ksiazka.ISBN)
        if existing:
            self.magazyn.usun(ksiazka.ISBN)
        self.magazyn.dodaj(ksiazka)


class RepozytoriumUzytkownika:
    """Adapter magazynu użytkowników do FasadyEncji"""
    def __init__(self):
        self.magazyn = MagazynUzytkownikow()
        self._next_id = 1

    def rejestrujUzytkownika(self, uzytkownik):
        uzytkownik.id = self._next_id
        self._next_id += 1
        self.magazyn.dodaj(uzytkownik)

    def znajdzUzytkownikaPoEmailu(self, email):
        for u in self.magazyn.pobierzListeUzytkownikow():
            if u.pobierzEmail() == email:
                return u
        return None

    def czyIstnieje(self, email):
        return self.znajdzUzytkownikaPoEmailu(email) is not None

    def usun(self, idUzytkownika):
        self.magazyn.usun(idUzytkownika)

    def pobierzDaneUzytkownika(self, idUzytkownika):
        return self.magazyn.pobierz(idUzytkownika)

    def aktualizujDaneUzytkownika(self, uzytkownik):
        # nadpisujemy
        existing = self.magazyn.pobierz(uzytkownik.id)
        if existing:
            self.magazyn.usun(uzytkownik.id)
        self.magazyn.dodaj(uzytkownik)


class RepozytoriumZamowien:
    """Adapter magazynu zamówień do FasadyEncji"""
    def __init__(self):
        self.magazyn = MagazynZamowien()

    def zapiszZamowienie(self, zamowienie):
        self.magazyn.dodaj(zamowienie)

    def pobierzHistorieDlaKlienta(self, idKlienta):
        return [z for z in self.magazyn.pobierzListeZamowien() if z.klient.id == idKlienta]

    def pobierzWszystkieZamowienia(self):
        return self.magazyn.pobierzListeZamowien()


def przygotuj_system():
    """
    Przygotowuje cały system PU03 bez mockowania.
    Zwraca: encje (fasadę), kontroler (None), klienta testowego, placeholder (None)
    """
    repo_ksiazek = RepozytoriumKsiazek()
    repo_uzytkownika = RepozytoriumUzytkownika()
    repo_zamowien = RepozytoriumZamowien()

    encje = FasadaEncji(
        repoKsiazek=repo_ksiazek,
        repoUzytkownika=repo_uzytkownika,
        repoZamowien=repo_zamowien,
        fabrykaKsiazek=FabrykaKsiazek(),
        dekoratorRabatu=DekoratorRabatuLojalnosciowego  # <- przekazujemy klasę, nie instancję
    )

    # dodanie przykładowego klienta
    klient = Klient("Jan", "Kowalski", "jan@test.pl", "haslo", "Adres 1", False)
    repo_uzytkownika.rejestrujUzytkownika(klient)

    kontrola = None
    placeholder = None

    return encje, kontrola, klient, placeholder

