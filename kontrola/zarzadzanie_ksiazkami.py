from .proces_zarzadzania import ProcesZarzadzania


# Klasa konkretna - dziedziczy po szablonie (Generalizacja)
class ZarzadzanieKsiazkami(ProcesZarzadzania):

    # Implementacja kroku abstrakcyjnego
    def _wykonajOperacjeNaEncji(self):
        print("ZarzadzanieKsiazkami: Wykonuję specyficzne operacje na książkach...")
        # STUB
        raise NotImplementedError("Logika zarządzania książkami nie jest zaimplementowana.")