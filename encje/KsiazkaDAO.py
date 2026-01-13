from typing import List, Optional
from encje.IRepozytoriumKsiazek import IRepozytoriumKsiazek
from encje.IKsiazka import IKsiazka
from encje.KsiazkaPapierowa import KsiazkaPapierowa
from encje.MagazynKsiazek import MagazynKsiazek


class KsiazkaDAO(IRepozytoriumKsiazek):

    def __init__(self):
        # Asocjacja z MagazynKsiazek (warstwa danych)
        self._ksiazki: List[IKsiazka] = []

    def dodajKsiazke(self, ksiazka: IKsiazka) -> None:
        self._ksiazki.append(ksiazka)

    def usunKsiazke(self, ISBN: int) -> None:
        self._ksiazki = [k for k in self._ksiazki if k.ISBN != ISBN]

    def pobierzWszystkie(self) -> List[IKsiazka]:
        return self._ksiazki.copy()

    def aktualizujDane(self, ksiazka: IKsiazka) -> None:
        pass

    def pobierzPoISBN(self, ISBN: int) -> Optional[IKsiazka]:
        for k in self._ksiazki:
            if k.ISBN == ISBN:
                return k
        return None

    def aktualizujStan(self, ISBN: int, nowyStan: int) -> None:
        ksiazka = self.pobierzPoISBN(ISBN)
        if isinstance(ksiazka, KsiazkaPapierowa):
            ksiazka.stanMagazynowy = nowyStan
        else:
            raise TypeError(
                f"Ksiażka o ISBN {ISBN} jest typu {type(ksiazka).__name__}, nie można zmienić stanu magazynowego.")