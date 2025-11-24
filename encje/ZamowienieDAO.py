from typing import List
from encje.IRepozytoriumZamowien import IRepozytoriumZamowien
from encje.Zamowienie import Zamowienie
from encje.Klient import Klient
from encje.MagazynZamowien import MagazynZamowien

# wzorzec, oddzielić logikę dostępu do bazy danych od logiki aplikacji

class ZamowienieDAO(IRepozytoriumZamowien):
    def __init__(self):
        self._magazyn = MagazynZamowien()

    def zapiszZamowienie(self, zamowienie: Zamowienie):
        print("DAO: Zapisuję zamówienie do Magazynu...")
        self._magazyn.dodaj(zamowienie)

    def pobierzHistorieDlaKlienta(self, idKlienta: int) -> List[Zamowienie]:
        return self._magazyn.pobierz_dla_klienta(idKlienta)

    def pobierzWszystkieZamowienia(self) -> List[Zamowienie]:
        return self._magazyn.pobierz_wszystkie()
