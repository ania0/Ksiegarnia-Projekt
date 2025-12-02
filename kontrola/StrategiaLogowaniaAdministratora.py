from kontrola.IStrategiaUwierzytelniania import IStrategiaUwierzytelniania
from encje.IEncjeFasada import IEncjeFasada
from encje.Uzytkownik import Uzytkownik
from typing import Optional



class StrategiaLogowanieAdministratora(IStrategiaUwierzytelniania):
    def __init__(self, fasada_encji: IEncjeFasada):
        self._fasada_encji = fasada_encji

    def uwierzytelnij(self, email: str, hashHasla: str) -> Optional[Uzytkownik]:
        # Tymczasowa logika: jeśli email kończy się na 'admin.com', traktujemy jako admina
        if email.endswith("admin.com"):
            uzytkownik = self._fasada_encji.znajdzUzytkownikaPoEmailu(email)
            return uzytkownik
        return None
