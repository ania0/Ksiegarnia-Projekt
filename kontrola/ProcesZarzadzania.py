# from abc import ABC, abstractmethod
# from encje.IEncjeFasada import IEncjeFasada
# from encje.Uzytkownik import Uzytkownik
#
# class ProcesZarzadzania(ABC):
#     def __init__(self, fasada_encji: IEncjeFasada, uzytkownik: Uzytkownik):
#         self._fasada_encji = fasada_encji
#         self._uzytkownik = uzytkownik
#
#     def wykonajZarzadzanie(self):
#         print("ProcesZarzadzania (Szablon): Start.")
#         if self._sprawdzUprawnienia():
#             self._wykonajOperacjeNaEncji()
#         else:
#             print("Brak uprawnień do wykonania tej operacji.")
#
#     def _sprawdzUprawnienia(self) -> bool:
#         print("ProcesZarzadzania: Sprawdzam uprawnienia...")
#         return self._uzytkownik is not None
#
#     @abstractmethod
#     def _wykonajOperacjeNaEncji(self):
#         pass


# class ProcesZarzadzania(ABC):
#     def __init__(self, fasada_encji: IEncjeFasada, uzytkownik: Uzytkownik):
#         self._fasada_encji = fasada_encji
#         self._uzytkownik = uzytkownik
#
#     def wykonajZarzadzanie(self):
#         print("ProcesZarzadzania (Szablon): Start.")
#         if self._sprawdzUprawnienia():
#             self._wykonajOperacjeNaEncji()
#         else:
#             print("Brak uprawnień do wykonania tej operacji.")
#
#     def _sprawdzUprawnienia(self) -> bool:
#         print("ProcesZarzadzania: Sprawdzam uprawnienia...")
#         return self._uzytkownik is not None
#
#     @abstractmethod
#     def _wykonajOperacjeNaEncji(self):
#         pass

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

