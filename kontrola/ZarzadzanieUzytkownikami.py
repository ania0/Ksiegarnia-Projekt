from kontrola.ProcesZarzadzania import ProcesZarzadzania
from encje.IEncjeFasada import IEncjeFasada

class ZarzadzanieUzytkownikami(ProcesZarzadzania):
    def _wykonajOperacjeNaEncji(self):
        print("ZarzadzanieUzytkownikami: Wykonuję operacje na kontach...")
        raise NotImplementedError("PU: Zarządzanie użytkownikami niezaimplementowane.")