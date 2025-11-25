from encje.IEncjeFasada import IEncjeFasada
from encje.Uzytkownik import Uzytkownik
from typing import Optional

class ProcesUsuwaniaKonta:
    def __init__(self, fasada_encji: IEncjeFasada, uzytkownik: Optional[Uzytkownik] = None):
        """
        :param fasada_encji: Fasada encji do operacji CRUD
        :param uzytkownik: obiekt Uzytkownik do usunięcia; jeśli None, można wprowadzić logikę pobrania aktualnie zalogowanego
        """
        self._fasada_encji = fasada_encji
        self._uzytkownik = uzytkownik

    def wykonaj(self):
        print("ProcesUsuwaniaKonta: Rozpoczynam...")

        if self._uzytkownik is None:
            print("ProcesUsuwaniaKonta: Brak wskazanego użytkownika do usunięcia.")
            return None

        # Sprawdzenie, czy użytkownik faktycznie istnieje w bazie
        istnieje = self._fasada_encji.czyIstnieje(self._uzytkownik.email)
        if not istnieje:
            print(f"ProcesUsuwaniaKonta: Użytkownik {self._uzytkownik.email} nie istnieje w bazie!")
            return None

        # Usunięcie użytkownika przez fasadę
        self._fasada_encji.usun(self._uzytkownik.id)
        print(f"ProcesUsuwaniaKonta: Użytkownik {self._uzytkownik.email} został usunięty.")
        return True
