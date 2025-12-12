from typing import List, Optional
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

    def aktualizujDane(self, ksiazka: IKsiazka, nowyTytul: Optional[str], nowyAutor: Optional[str],
                       nowyGatunek: Optional[str], nowaCena: Optional[float], nowyOpis: Optional[str]) -> Optional[str]:
        """
        Realizacja diagramu sekwencji: Sprawdza wartości i ustawia je przez settery IKsiazka.
        """

        # 1.1: [nowyTytul != Null] -> ustawTytul
        if nowyTytul:
            ksiazka.ustawTytul(nowyTytul)

        # 1.3: [nowyAutor != Null] -> ustawAutora
        if nowyAutor:
            ksiazka.ustawAutora(nowyAutor)

        # 1.5: [nowyGatunek != Null] -> ustawGatunek
        if nowyGatunek:
            ksiazka.ustawGatunek(nowyGatunek)

        # Walidacja ceny z diagramu
        if nowaCena is not None:
            # 1.11: [nowaCena <= 0] -> return UjemnaCena
            if nowaCena <= 0:
                return "UjemnaCena"
            # 1.7: [nowaCena > 0] -> ustawCene
            else:
                ksiazka.ustawCene(nowaCena)

        # 1.9: [nowyOpis != Null] -> ustawOpis
        if nowyOpis:
            ksiazka.ustawOpis(nowyOpis)

        # Persystencja (mimo że diagram kończy się na encji, w kodzie musimy upewnić się, że DAO "widzi" zmianę)
        # Przekazujemy zaktualizowany obiekt do DAO
        self._repoKsiazek.aktualizujDane(ksiazka)

        return None  # 1.12: None (sukces)

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

