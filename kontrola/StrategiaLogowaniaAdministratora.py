from encje.Administrator import Administrator
from kontrola.IStrategiaUwierzytelniania import IStrategiaUwierzytelniania
from encje.IEncjeFasada import IEncjeFasada
from encje.Uzytkownik import Uzytkownik
from typing import Optional



class StrategiaLogowanieAdministratora(IStrategiaUwierzytelniania):
    def __init__(self, fasada_encji: IEncjeFasada):
        self._fasada_encji = fasada_encji

    def uwierzytelnij(self, email: str, haslo: str) -> Optional[Uzytkownik]:
        # 1.1: znajdzUzytkownikaPoEmailu
        uzytkownik = self._fasada_encji.znajdzUzytkownikaPoEmailu(email)

        if uzytkownik is not None:
            # SPRAWDZENIE TYPU: Logowanie Admina tylko dla Administratorów
            if isinstance(uzytkownik, Administrator):
                if uzytkownik.weryfikujHaslo(haslo):
                    return uzytkownik
            # [uzytkownik == null] -> 1.r: null

        return None