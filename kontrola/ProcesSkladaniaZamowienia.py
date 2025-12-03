from encje.IEncjeFasada import IEncjeFasada
from encje.Klient import Klient

class ProcesSkladaniaZamowienia:
    def __init__(self, fasada_encji: IEncjeFasada, uzytkownik: Klient):
        self._fasada_encji = fasada_encji
        self._uzytkownik = uzytkownik

    def wykonajSkladanieZamowienia(self, id_klienta, lista_ISBN) -> None:
        pass