from kontrola.IStrategiaUwierzytelniania import IStrategiaUwierzytelniania
from encje.IEncjeFasada import IEncjeFasada
from encje.Uzytkownik import Uzytkownik
from typing import Optional



class StrategiaLogowanieKlienta(IStrategiaUwierzytelniania):
    def __init__(self, fasada_encji: IEncjeFasada):
        self._fasada_encji = fasada_encji

    def uwierzytelnij(self, email: str, haslo: str) -> Optional[Uzytkownik]:
        # Tymczasowa logika: szukamy użytkownika po emailu w fasadzie
        uzytkownik = self._fasada_encji.znajdzUzytkownikaPoEmailu(email)
        if uzytkownik is not None:
            # Na tym etapie możemy przyjąć, że hasło pasuje (testowe PU)
            return uzytkownik
        return None
