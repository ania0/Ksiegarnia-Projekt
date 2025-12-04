
from encje.ICena import ICena
from encje.IEncjeFasada import IEncjeFasada
from encje.Uzytkownik import Uzytkownik
from encje.Klient import Klient
from encje.Zamowienie import Zamowienie
from encje.IKsiazka import IKsiazka
from encje.FabrykaKsiazek import FabrykaKsiazek
from encje.DekoratorRabatuLojalnosciowego import DekoratorRabatuLojalnosciowego
from encje.IRepozytoriumKsiazek import IRepozytoriumKsiazek
from encje.IRepozytoriumUzytkownika import IRepozytoriumUzytkownika
from encje.IRepozytoriumZamowien import IRepozytoriumZamowien
from typing import List # TU


class FasadaEncji(IEncjeFasada):

    def __init__(self, repoKsiazek: IRepozytoriumKsiazek,
                 repoUzytkownika: IRepozytoriumUzytkownika,
                 repoZamowien: IRepozytoriumZamowien,
                 fabrykaKsiazek: FabrykaKsiazek,
                 dekoratorRabatu: DekoratorRabatuLojalnosciowego):
        self._repoKsiazek = repoKsiazek
        self._repoUzytkownika = repoUzytkownika
        self._repoZamowien = repoZamowien
        self._fabrykaKsiazek = fabrykaKsiazek
        self._dekoratorRabatu = dekoratorRabatu
        self._next_id = 1  # licznik ID do wyswietlania

    # UŻYTKOWNICY
    def rejestrujUzytkownika(self, uzytkownik: Uzytkownik) -> None:
        self._repoUzytkownika.rejestrujUzytkownika(uzytkownik)

    def znajdzUzytkownikaPoEmailu(self, email: str) -> Uzytkownik:
        return self._repoUzytkownika.znajdzUzytkownikaPoEmailu(email)

    def czyIstnieje(self, email: str) -> bool:
        return self._repoUzytkownika.czyIstnieje(email)

    def usun(self, idUzytkownika: int) -> None:
        self._repoUzytkownika.usun(idUzytkownika)

    def pobierzDaneUzytkownika(self, idUzytkownika: int) -> Uzytkownik:
        return self._repoUzytkownika.pobierzDaneUzytkownika(idUzytkownika)

    # KSIĄŻKI
    def dodajKsiazke(self, ksiazka: IKsiazka) -> None:
        ksiazka.id = self._next_id # dodałam tu pole id do wyswietlania
        self._next_id += 1
        self._repoKsiazek.dodajKsiazke(ksiazka)

    def usunKsiazke(self, ISBN: int) -> None:
        self._repoKsiazek.usunKsiazke(ISBN)

    def pobierzWszystkie(self) -> List[IKsiazka]:
        return self._repoKsiazek.pobierzWszystkie()

    def aktualizujDane(self, ksiazka: IKsiazka) -> None:
        self._repoKsiazek.aktualizujStan(ksiazka)

    def pobierzPoISBN(self, ISBN: int) -> IKsiazka:
        return self._repoKsiazek.pobierzPoISBN(ISBN)

    def aktualizujStan(self, ISBN: int, nowyStan: int) -> None:
        self._repoKsiazek.aktualizujStan(ISBN, nowyStan)

    # ZAMÓWIENIA
    def zapiszZamowienie(self, zamowienie: Zamowienie) -> None:
        self._repoZamowien.zapiszZamowienie(zamowienie)

    def pobierzHistorieDlaKlienta(self, idKlienta: int) -> List[Zamowienie]:
        return self._repoZamowien.pobierzHistorieDlaKlienta(idKlienta)

    def pobierzWszystkieZamowienia(self) -> List[Zamowienie]:
        return self._repoZamowien.pobierzWszystkieZamowienia()

    # DEKORATORY / CENA
    def obliczCeneOstateczna(self, zamowienie: Zamowienie, klient: Klient) -> float:
        komponent: ICena = zamowienie  # Zamowienie implementuje ICena

        if klient.klientLojalny:
            dekorator = self._dekoratorRabatuLojalnosciowego(komponent)
            return dekorator.obliczCene()
        else:
            return komponent.obliczCene()

