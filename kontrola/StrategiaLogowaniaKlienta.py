from kontrola.IStrategiaUwierzytelniania import IStrategiaUwierzytelniania
from encje.IEncjeFasada import IEncjeFasada
from encje.Uzytkownik import Uzytkownik
from typing import Optional



class StrategiaLogowanieKlienta(IStrategiaUwierzytelniania):
    def __init__(self, fasada_encji: IEncjeFasada):
        self._fasada_encji = fasada_encji

    def uwierzytelnij(self, email: str, hashHasla: str) -> Optional[Uzytkownik]:
        pass


