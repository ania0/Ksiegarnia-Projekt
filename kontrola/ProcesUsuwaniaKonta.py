from encje.IEncjeFasada import IEncjeFasada
from encje.Klient import Klient
from typing import Optional


class ProcesUsuwaniaKonta:
    def __init__(self, fasada_encji: IEncjeFasada, uzytkownik: Optional[Klient] = None):
        """
        :param fasada_encji: Fasada encji do operacji CRUD
        :param uzytkownik: obiekt Uzytkownik do usunięcia; jeśli None, można wprowadzić logikę pobrania aktualnie zalogowanego
        """
        self._fasada_encji = fasada_encji
        self._uzytkownik = uzytkownik

    def wykonajUsuwanie(self) -> None:
        pass
