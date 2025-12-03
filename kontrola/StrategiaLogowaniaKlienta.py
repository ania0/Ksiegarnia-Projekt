from kontrola.IStrategiaUwierzytelniania import IStrategiaUwierzytelniania
from encje.IEncjeFasada import IEncjeFasada
from encje.Uzytkownik import Uzytkownik
from typing import Optional



class StrategiaLogowanieKlienta(IStrategiaUwierzytelniania):
    def __init__(self, fasada_encji: IEncjeFasada):
        self._fasada_encji = fasada_encji

    def uwierzytelnij(self, email: str, haslo: str) -> Optional[Uzytkownik]:
        # 1.1: znajdzUzytkownikaPoEmailu
        uzytkownik = self._fasada_encji.znajdzUzytkownikaPoEmailu(email)

        if uzytkownik is not None:
            # 1.2: weryfikujHaslo(haslo)
            if uzytkownik.weryfikujHaslo(haslo):
                # 1.r: uzytkownik
                return uzytkownik
            # else weryfikujHaslo == false -> 1.r: null
            return None

            # [uzytkownik == null] -> 1.r: null
        return None
