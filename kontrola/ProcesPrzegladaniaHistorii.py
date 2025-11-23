from encje.IEncjeFasada import IEncjeFasada


class ProcesPrzegladaniaHistorii:
    def __init__(self, fasada_encji: IEncjeFasada):
        self._fasada_encji = fasada_encji

    def wykonaj(self):
        print("ProcesPrzegladaniaHistorii: Rozpoczynam...")
        raise NotImplementedError("PU: Logika ProcesPrzegladaniaHistorii nie jest zaimplementowana.")