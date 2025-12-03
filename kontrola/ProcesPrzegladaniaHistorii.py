from encje.IEncjeFasada import IEncjeFasada
from encje.Klient import Klient
from encje.Zamowienie import Zamowienie
from typing import List, Optional


class ProcesPrzegladaniaHistorii:
    """
    Proces przeglądania historii zamówień dla klienta.
    """

    def __init__(self, fasada_encji: IEncjeFasada, uzytkownik: Klient):
        self._fasada_encji = fasada_encji
        self._uzytkownik = uzytkownik

    def __init__(self, fasada_encji: IEncjeFasada, uzytkownik: Optional[Klient]):  # Uzytkownik może być None
        self._fasada_encji = fasada_encji
        self._uzytkownik = uzytkownik

    # Metoda musi przyjąć id_klienta, aby pasować do wywołania w FasadaKontroli
    def wykonajPrzegladanieHistorii(self, id_klienta: int) -> List[Zamowienie]:
        """
        Pobiera historię zamówień dla klienta o podanym ID.
        """
        # Używamy ID przekazanego w argumencie, a nie ID zalogowanego,
        # bo to ID jest przekazywane z zewnątrz.

        # Opcjonalna weryfikacja (zgodna z architekturą)
        if self._uzytkownik is None:
            # Użytkownik musi być zalogowany, żeby przeglądać (chyba że to admin)
            # Jeśli chcemy, by klient przeglądał tylko swoją historię:
            if self._uzytkownik is None or self._uzytkownik.pobierzId() != id_klienta:
                raise PermissionError("Brak autoryzacji do przeglądania tej historii.")

        historia = self._fasada_encji.pobierzHistorieDlaKlienta(id_klienta)  # Używamy ID z argumentu
        # W trybie testowym można dodatkowo wyświetlić historię w terminalu
        print(f"Historia zamówień dla klienta {self._uzytkownik.imie} {self._uzytkownik.nazwisko}:")
        for zam in historia:
            print(f"- Zamówienie ID {zam.pobierzId()} z dnia {zam._data} o statusie {zam._status}")

        return historia
