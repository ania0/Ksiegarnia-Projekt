from kontrola.ProcesZarzadzania import ProcesZarzadzania
from encje.IEncjeFasada import IEncjeFasada

class ZarzadzanieKsiazkami(ProcesZarzadzania):
    def _wykonajOperacjeNaEncji(self):
        print("ZarzadzanieKsiazkami: Wykonuję operacje na katalogu (Dodaj/Edytuj/Usuń)...")
        raise NotImplementedError("PU: Zarządzanie książkami niezaimplementowane.")