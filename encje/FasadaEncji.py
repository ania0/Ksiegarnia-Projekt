from encje.Uzytkownik import Uzytkownik
from encje.Zamowienie import Zamowienie
from encje.Klient import Klient
from encje.IKsiazka import IKsiazka
from typing import List

from encje.IRepozytoriumKsiazek import IRepozytoriumKsiazek
from encje.IRepozytoriumUzytkownika import IRepozytoriumUzytkownika
from encje.IRepozytoriumZamowien import IRepozytoriumZamowien
from encje.IEncjeFasada import IEncjeFasada
from encje.FabrykaKsiazek import FabrykaKsiazek
from encje.DekoratorRabatuLojalnosciowego import DekoratorRabatuLojalnosciowego
from encje.ICena import ICena


# fasada dla encji – kl pośrednicząca między logiką biznes a repozytoriami - ukrywa szczegóły i deleguje zadania do repo
class FasadaEncji:

    # konstruktor fasady
    def __init__(self, repoKsiazek: IRepozytoriumKsiazek,
                 repoUzytkownika: IRepozytoriumUzytkownika,
                 repoZamowien: IRepozytoriumZamowien,
                 fabrykaKsiazek: FabrykaKsiazek):

        self.repoKsiazek = repoKsiazek
        self.repoUzytkownika = repoUzytkownika
        self.repoZamowien = repoZamowien
        self.fabrykaKsiazek = fabrykaKsiazek

    # rejestracja użytk delegowana do repo
    def rejestrujUzytkownika(self, uzytkownik):
        self.repoUzytkownika.rejestrujUzytkownika(uzytkownik)

    def znajdzUzytkownikaPoLoginie(self, email: str) -> Uzytkownik:
        return self.repoUzytkownika.znajdzUzytkownikaPoEmail(email)

    def czyIstnieje(self, email: str) -> bool:
        return self.repoUzytkownika.czyIstnieje(email)

    def usun(self, idUzytkownika: int):
        self.repoUzytkownika.usun(idUzytkownika)

    def pobierzDaneUzytkownika(self, idUzytkownika: int) -> Uzytkownik:
        return self.repoUzytkownika.pobierzDaneUzytkownika(idUzytkownika)


    # typ tylko IKsiazka
    def dodajKsiazke(self, ksiazka: IKsiazka):
        self.repoKsiazek.dodajKsiazke(ksiazka)

    def usunKsiazke(self, idKsiazki: int):
        self.repoKsiazek.usunKsiazke(idKsiazki)

    def pobierzWszystkie(self) -> List[IKsiazka]:
        return self.repoKsiazek.pobierzWszystkie()

    def AktualizujDane(self, ksiazka: IKsiazka):
        self.repoKsiazek.AktualizujDane(ksiazka)

    def pobierzPoId(self, id: int) -> IKsiazka:
        return self.repoKsiazek.pobierzPoId(id)

    def aktualizujStan(self, idKsiazki: int, nowyStan: int):
        self.repoKsiazek.aktualizuj(idKsiazki, nowyStan)


    def zapiszZamowienie(self, zamowienie: Zamowienie):
        self.repoZamowien.zapiszZamowienie(zamowienie)

    def pobierzHistorieDlaKlienta(self, idKlienta: int) -> List[Zamowienie]:
        return self.repoZamowien.pobierzHistorieDlaKlienta(idKlienta)

    def pobierzWszystkieZamowienia(self) -> List[Zamowienie]:
        return self.repoZamowien.pobierzWszystkieZamowienia()


    # dekoarator - zamówienie implementuje ICena
    # Jeśli klient lojalny → owijamy zamówienie dekoratorem dodającym rabat, bez modyfikowania kl Zamowienie
    def obliczCeneOstateczna(self, zamowienie: Zamowienie, klient: Klient) -> float:
        komponent_ceny: ICena = zamowienie
        if klient.klientLojalny:
            komponent_ceny = DekoratorRabatuLojalnosciowego(komponent_ceny)
        return komponent_ceny.obliczCene()
