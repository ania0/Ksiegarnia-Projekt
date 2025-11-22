from encje.IEncjeFasada import IEncjeFasada


class ProcesUsuwaniaKonta:
    def __init__(self, fasada_encji: IEncjeFasada):
        self._fasada_encji = fasada_encji

    def wykonaj(self):
        print("ProcesUsuwaniaKonta: Rozpoczynam...")
        # STUB
        raise NotImplementedError("PU: Logika ProcesUsuwaniaKonta nie jest zaimplementowana.")