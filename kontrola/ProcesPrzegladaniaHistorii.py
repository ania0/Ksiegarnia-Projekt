from encje.IEncjeFasada import IEncjeFasada
from encje.Klient import Klient
from encje.Zamowienie import Zamowienie
from typing import List


class ProcesPrzegladaniaHistorii:
    """
    Proces przeglądania historii zamówień dla klienta.
    """

    def __init__(self, fasada_encji: IEncjeFasada, uzytkownik: Klient):
        self._fasada_encji = fasada_encji
        self._uzytkownik = uzytkownik

    def wykonajPrzegladanieHistorii(self) -> List[Zamowienie]:
        """
        Pobiera historię zamówień klienta i zwraca ją w postaci listy.
        """
        if self._uzytkownik is None:
            raise ValueError("Brak przypisanego użytkownika.")

        historia = self._fasada_encji.pobierzHistorieDlaKlienta(self._uzytkownik.pobierzId())

        # W trybie testowym można dodatkowo wyświetlić historię w terminalu
        print(f"Historia zamówień dla klienta {self._uzytkownik.imie} {self._uzytkownik.nazwisko}:")
        for zam in historia:
            print(f"- Zamówienie ID {zam.pobierzId()} z dnia {zam._data} o statusie {zam._status}")

        return historia
