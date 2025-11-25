from typing import List
from encje.IRepozytoriumKsiazek import IRepozytoriumKsiazek
from encje.IKsiazka import IKsiazka
from encje.MagazynKsiazek import MagazynKsiazek
#  wzorzec, oddzielić logikę dostępu do bazy danych od logiki aplikacji


# class KsiazkaDAO(IRepozytoriumKsiazek):
#     def __init__(self):
#         # Relacja z diagramu: DAO -> Magazyn
#         self._magazyn = MagazynKsiazek()
#         pass
#
#     def dodajKsiazke(self, ksiazka: IKsiazka):
#         print("DAO: Dodaję książkę do Magazynu...")
#         self._magazyn.dodaj(ksiazka)
#         pass
#
#     def usunKsiazke(self, ISBN : int):
#         self._magazyn.usun(ISBN)
#         pass
#
#     def pobierzWszystkie(self) -> List[IKsiazka]:
#         return self._magazyn.pobierz_wszystkie()
#         pass
#
#     def AktualizujDane(self, ksiazka: IKsiazka):
#         self._magazyn.aktualizuj(ksiazka)
#         pass
#
#     def pobierzPoISBN(self, ISBN: int) -> IKsiazka:
#         return self._magazyn.znajdz_po_isbn(ISBN)
#         pass

    # def aktualizujStan(self, ISBN: int, nowyStan: int):
    #     # Logika: pobierz z magazynu -> zmień stan -> (magazyn trzyma referencję, więc się zaktualizuje)
    #     ksiazka = self._magazyn.znajdz_po_id(ISBN)
    #     if ksiazka:
    #         # Zakładamy, że obiekt IKsiazka ma pole stanMagazynowy
    #         # Jeśli IKsiazka to interfejs, upewnij się, że ta operacja jest tam dozwolona,
    #         # lub rzutuj na konkretną klasę Ksiazka
    #         if hasattr(ksiazka, 'stanMagazynowy'):
    #              ksiazka.stanMagazynowy = nowyStan
    #         else:
    #              print("Błąd: Obiekt nie ma pola stanMagazynowy")


from typing import List
from encje.IRepozytoriumKsiazek import IRepozytoriumKsiazek
from encje.IKsiazka import IKsiazka

class KsiazkaDAO(IRepozytoriumKsiazek):

    def __init__(self):
        # Relacja z diagramu: DAO -> Magazyn
        self.___magazyn: MagazynKsiazek = None
        pass

    def dodajKsiazke(self, ksiazka: IKsiazka):
        print("DAO: Dodaję książkę do Magazynu...")
        raise NotImplementedError("dodajKsiazke - niezaimplementowane.")

    def usunKsiazke(self, ISBN: int):
        raise NotImplementedError("usunKsiazke - niezaimplementowane.")

    def pobierzWszystkie(self) -> List[IKsiazka]:
        return []  # domyślna wartość

    def AktualizujDane(self, ksiazka: IKsiazka):
        raise NotImplementedError("AktualizujDane - niezaimplementowane.")

    def pobierzPoISBN(self, ISBN: int) -> IKsiazka:
        return None  # domyślna wartość

    def aktualizujStan(self, ISBN: int, nowyStan: int):
        raise NotImplementedError("aktualizujStan - niezaimplementowane.")
