from encje.IEncjeFasada import IEncjeFasada
from encje.Administrator import Administrator
from typing import List
from encje.Zamowienie import Zamowienie


class ProcesPrzegladaniaRaportu:
    def __init__(self, fasada_encji: IEncjeFasada):
        # Asocjacja z fasadą encji (warstwa danych)
        self._fasada_encji: IEncjeFasada = fasada_encji
        # Użytkownik wykonujący operację (administrator)
        self._uzytkownik: Administrator = None

    def wykonajPrzegladanieRaportu(self) -> List[Zamowienie]:
        """
        Pobiera listę wszystkich zamówień i wyświetla je w terminalu.
        """
        if not self._uzytkownik:
            raise ValueError("Brak przypisanego użytkownika wykonującego operację.")

        lista_zamowien: List[Zamowienie] = self._fasada_encji.pobierzWszystkieZamowienia()

        print("Raport wszystkich zamówień:")
        for zamowienie in lista_zamowien:
            klient = zamowienie.pobierzKlienta()
            print(
                f"- Zamówienie ID: {zamowienie.pobierzId()}, klient: {klient.pobierzId() if klient else 'brak'}, cena: {zamowienie.obliczCene()} zł")

        return lista_zamowien