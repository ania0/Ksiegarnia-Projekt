from encje.IEncjeFasada import IEncjeFasada
from encje.Klient import Klient

class ProcesPrzegladaniaHistorii:
    def __init__(self, fasada_encji: IEncjeFasada, uzytkownik: Klient):
        self._fasada_encji = fasada_encji
        self._uzytkownik = uzytkownik

    def wykonajPrzegladanieHistorii(self) -> None:
        # print("ProcesPrzegladaniaHistorii: Rozpoczynam...")
        raise NotImplementedError("PU: Logika ProcesPrzegladaniaHistorii nie jest zaimplementowana.")