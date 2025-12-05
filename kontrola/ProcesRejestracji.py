

from encje.IEncjeFasada import IEncjeFasada
from encje.Klient import Klient  # Klient dziedziczy z Uzytkownik, więc używamy bardziej specyficznej klasy


class ProcesRejestracji:
    def __init__(self, fasada_encji: IEncjeFasada):
        self._fasada_encji = fasada_encji

    def wykonajRejestracje(self, email: str, haslo: str) -> None:
        # Proces pusty – wszystkie dane klienta tworzymy w main.py
        pass
