from kontrola.IStrategiaUwierzytelniania import IStrategiaUwierzytelniania
from encje.IEncjeFasada import IEncjeFasada
from encje.Uzytkownik import Uzytkownik


class StrategiaLogowanieKlienta(IStrategiaUwierzytelniania):
    def __init__(self, fasada_encji: IEncjeFasada):
        self._fasada_encji = fasada_encji

    def uwierzytelnij(self, daneLogowania: str, haslo: str) -> Uzytkownik:
        print("StrategiaKlienta: Weryfikacja w bazie danych...")
        uzytkownik = self._fasada_encji.znajdzUzytkownikaPoLoginie(daneLogowania)

        if uzytkownik:
            return uzytkownik
        return None