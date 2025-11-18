from encje.IEncjeFasada import IEncjeFasada


class ProcesPrzegladaniaRaportu:
    def __init__(self, fasada_encji: IEncjeFasada):
        self._fasada_encji = fasada_encji

    def wykonaj(self):
        print("ProcesPrzegladaniaRaportu: Rozpoczynam...")
        # STUB
        raise NotImplementedError("PU: Logika ProcesPrzegladaniaRaportu nie jest zaimplementowana.")