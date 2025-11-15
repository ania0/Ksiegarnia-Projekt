from encje.iencje_fasada import IEncjeFasada


class ProcesSkladaniaZamowienia:
    def __init__(self, fasada_encji: IEncjeFasada):
        self._fasada_encji = fasada_encji

    def wykonaj(self, koszyk):
        print("ProcesSkladaniaZamowienia: Rozpoczynam...")
        # STUB (do zaimplementowania w Zadaniu 4)
        raise NotImplementedError("Zadanie 4: Logika ProcesSkladaniaZamowienia nie jest zaimplementowana.")