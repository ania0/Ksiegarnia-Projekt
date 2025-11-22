from encje.IEncjeFasada import IEncjeFasada


class ProcesRejestracji:
    def __init__(self, fasada_encji: IEncjeFasada):
        self._fasada_encji = fasada_encji

    def wykonaj(self):
        print("ProcesRejestracji: Rozpoczynam...")

        dane_stub = {"login": "nowy_user", "haslo": "123"}


        raise NotImplementedError("PU: Rejestracja niezaimplementowana.")