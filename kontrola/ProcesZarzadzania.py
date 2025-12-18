from abc import ABC, abstractmethod
from encje.IEncjeFasada import IEncjeFasada
from encje.Uzytkownik import Uzytkownik
from encje.Administrator import Administrator


class ProcesZarzadzania(ABC):
    """
    Abstrakcyjny proces zarządzania – szkielet.
    """

    def __init__(self, fasada_encji: IEncjeFasada, uzytkownik: Administrator):
        # Asocjacja z fasadą encji
        self._fasada_encji: IEncjeFasada = fasada_encji
        # Asocjacja z administratorem wykonującym operację
        self._uzytkownik: Administrator = uzytkownik

