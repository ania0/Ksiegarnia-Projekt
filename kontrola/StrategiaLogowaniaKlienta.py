from encje.Klient import Klient
from kontrola.IStrategiaUwierzytelniania import IStrategiaUwierzytelniania
from encje.IEncjeFasada import IEncjeFasada
from encje.Uzytkownik import Uzytkownik
from typing import Optional



class StrategiaLogowanieKlienta(IStrategiaUwierzytelniania):
    def __init__(self, fasada_encji: IEncjeFasada):
        self._fasada_encji = fasada_encji

    def uwierzytelnij(self, email: str, haslo: str):
        # 1.1 – znajdź użytkownika po e-mailu
        uzytkownik = self._fasada_encji.znajdzUzytkownikaPoEmailu(email)

        if uzytkownik is None:
            return None

        if uzytkownik.weryfikujHaslo(haslo):
            return uzytkownik
        else:
            return None
