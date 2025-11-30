from encje.IEncjeFasada import IEncjeFasada
from encje.Administrator import Administrator


class ProcesPrzegladaniaRaportu:
    def __init__(self, fasada_encji: IEncjeFasada):
        # Asocjacja z fasadą encji (warstwa danych)
        self._fasada_encji: IEncjeFasada = fasada_encji
        # Użytkownik wykonujący operację (administrator)
        self._uzytkownik: Administrator = None

    def wykonajPrzegladanieRaportu(self) -> None:
        raise NotImplementedError("wykonajPrzegladanieRaportu() nie jest jeszcze zaimplementowane.")
