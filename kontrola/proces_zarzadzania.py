from abc import ABC, abstractmethod
from encje.iencje_fasada import IEncjeFasada


# Klasa Abstrakcyjna - szablon
class ProcesZarzadzania(ABC):
    def __init__(self, fasada_encji: IEncjeFasada):
        self._fasada_encji = fasada_encji

    # Metoda Szablonowa
    def wykonajZarzadzanie(self):
        print("ProcesZarzadzania (Szablon): Start...")
        self._sprawdzUprawnienia()
        self._wykonajOperacjeNaEncji()
        print("ProcesZarzadzania (Szablon): Koniec.")

    # Chroniony krok 1 - STUB
    def _sprawdzUprawnienia(self):
        print("ProcesZarzadzania (Szablon): Sprawdzam uprawnienia...")
        raise NotImplementedError("Logika sprawdzania uprawnień nie jest zaimplementowana.")

    # Abstrakcyjny krok 2 - musi być zaimplementowany przez "dzieci"
    @abstractmethod
    def _wykonajOperacjeNaEncji(self):
        pass