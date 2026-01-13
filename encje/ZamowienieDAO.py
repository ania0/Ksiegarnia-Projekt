
from typing import List
from encje.IRepozytoriumZamowien import IRepozytoriumZamowien
from encje.Zamowienie import Zamowienie
from encje.Klient import Klient
from encje.MagazynZamowien import MagazynZamowien

class ZamowienieDAO(IRepozytoriumZamowien):
        """
        DAO odpowiedzialne za dostęp do danych Zamowien.
        """
        def __init__(self):
            # Asocjacja z MagazynZamowien (warstwa danych)
            self._magazyn = MagazynZamowien()

        def zapiszZamowienie(self, zamowienie: Zamowienie) -> None:
            """
            Zapisuje zamówienie do repozytorium.
            """
            self._magazyn._listaZamowien.append(zamowienie)

        def pobierzHistorieDlaKlienta(self, idKlienta: int) -> List[Zamowienie]:
            """
            Zwraca historię zamówień klienta.
            """
            historia = [
                z for z in self._magazyn._listaZamowien
                if z.pobierzKlienta() is not None and z.pobierzKlienta().pobierzId() == idKlienta
            ]
            return historia

        def pobierzWszystkieZamowienia(self) -> List[Zamowienie]:
            """
            Zwraca wszystkie zamówienia.
            """
            return list(self._magazyn._listaZamowien)