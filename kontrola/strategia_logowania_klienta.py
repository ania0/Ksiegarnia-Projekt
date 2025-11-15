from .istrategia_uwierzytelniania import IStrategiaUwierzytelniania
from encje.iencje_fasada import IEncjeFasada
from encje.modele import Uzytkownik


class StrategiaLogowaniaKlienta(IStrategiaUwierzytelniania):
    # Wstrzykiwanie zależności - strategia potrzebuje fasady Encji
    def __init__(self, fasada_encji: IEncjeFasada):
        self._fasada_encji = fasada_encji

    def uwierzytelnij(self, daneLogowania: str, haslo: str) -> Uzytkownik:
        print("StrategiaKlienta: Rozpoczynam uwierzytelnienie...")
        # To wywoła błąd STUB z FasadaEncji
        return self._fasada_encji.uwierzytelnijUzytkownika(daneLogowania, haslo)