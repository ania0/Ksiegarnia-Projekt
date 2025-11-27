from kontrola.IStrategiaUwierzytelniania import IStrategiaUwierzytelniania
from encje.IEncjeFasada import IEncjeFasada
from encje.Uzytkownik import Uzytkownik
from typing import Optional



class StrategiaLogowanieAdministratora(IStrategiaUwierzytelniania):
    def __init__(self, fasada_encji: IEncjeFasada):
        self._fasada_encji = fasada_encji

    def uwierzytelnij(self, email: str, hashHasla: str) -> Uzytkownik:
        # print("StrategiaAdmin: Weryfikacja uprawnień admina...")
        raise NotImplementedError("PU: Logika logowania administratora nie jest zaimplementowana.")
