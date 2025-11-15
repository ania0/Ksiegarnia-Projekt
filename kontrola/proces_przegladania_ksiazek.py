from encje.iencje_fasada import IEncjeFasada


class ProcesPrzegladaniaKsiazek:
    def __init__(self, fasada_encji: IEncjeFasada):
        self._fasada_encji = fasada_encji

    def wykonaj(self):
        print("ProcesPrzegladaniaKsiazek: Rozpoczynam...")
        # STUB
        raise NotImplementedError("PU: Logika ProcesPrzegladaniaKsiazek nie jest zaimplementowana.")