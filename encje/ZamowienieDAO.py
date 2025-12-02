# from typing import List
# from encje.IRepozytoriumZamowien import IRepozytoriumZamowien
# from encje.Zamowienie import Zamowienie
# from encje.Klient import Klient
# from encje.MagazynZamowien import MagazynZamowien

# wzorzec, oddzielić logikę dostępu do bazy danych od logiki aplikacji

# class ZamowienieDAO(IRepozytoriumZamowien):
#     def __init__(self):
#         self._magazyn = MagazynZamowien()
#
#     def zapiszZamowienie(self, zamowienie: Zamowienie):
#         print("DAO: Zapisuję zamówienie do Magazynu...")
#         self._magazyn.dodaj(zamowienie)
#         pass
#
#     def pobierzHistorieDlaKlienta(self, idKlienta: int) -> List[Zamowienie]:
#         return self._magazyn.pobierz_dla_klienta(idKlienta)
#
#     def pobierzWszystkieZamowienia(self) -> List[Zamowienie]:
#         return self._magazyn.pobierz_wszystkie()
#         pass

from typing import List
from encje.IRepozytoriumZamowien import IRepozytoriumZamowien
from encje.Zamowienie import Zamowienie
from encje.Klient import Klient
from encje.MagazynZamowien import MagazynZamowien

class ZamowienieDAO(IRepozytoriumZamowien):
        """
        DAO odpowiedzialne za dostęp do danych Zamowien.
        W tej fazie projektu zawiera tylko strukturę, a operacje nie mają implementacji.
        """

        def __init__(self):
            # Asocjacja z MagazynZamowien (warstwa danych)
            self._magazyn = MagazynZamowien()

        def zapiszZamowienie(self, zamowienie: Zamowienie) -> None:
            """
            Zapisuje zamówienie do repozytorium.
            Tymczasowa implementacja — metoda niezaimplementowana.
            """
            self._magazyn._listaZamowien.append(zamowienie)

        def pobierzHistorieDlaKlienta(self, idKlienta: int) -> List[Zamowienie]:
            """
            Zwraca historię zamówień klienta.
            Tymczasowa implementacja — zwraca pustą listę.
            """
            historia = [
                z for z in self._magazyn._listaZamowien
                if z.pobierzKlienta() is not None and z.pobierzKlienta().pobierzId() == idKlienta
            ]
            return historia

        def pobierzWszystkieZamowienia(self) -> List[Zamowienie]:
            """
            Zwraca wszystkie zamówienia.
            Tymczasowa implementacja — metoda niezaimplementowana.
            """
            return list(self._magazyn._listaZamowien)