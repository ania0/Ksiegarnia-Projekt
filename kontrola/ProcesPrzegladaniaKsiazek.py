from encje.IEncjeFasada import IEncjeFasada

class ProcesPrzegladaniaKsiazek:
    def __init__(self, fasada_encji: IEncjeFasada):
        self._fasada_encji = fasada_encji

    def wykonaj(self):
        print("ProcesPrzegladaniaKsiazek: Pobieram listę...")
        raise NotImplementedError("PU: Przeglądanie książek niezaimplementowane.")