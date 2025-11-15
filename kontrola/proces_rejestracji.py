from encje.iencje_fasada import IEncjeFasada


class ProcesRejestracji:
    def __init__(self, fasada_encji: IEncjeFasada):
        self._fasada_encji = fasada_encji

    def wykonaj(self, dane_rejestracji):
        print("ProcesRejestracji: Rozpoczynam...")
        # 1. Logika walidacji (pominięta)
        # 2. Wywołanie fasady Encji
        # To wywoła błąd STUB z UzytkownikDAO
        return self._fasada_encji.stworzKonto(dane_rejestracji)