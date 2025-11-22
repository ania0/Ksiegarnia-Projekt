from encje.IEncjeFasada import IEncjeFasada
from encje.Uzytkownik import Uzytkownik

class ProcesSkladaniaZamowienia:
    def __init__(self, fasada_encji: IEncjeFasada, uzytkownik: Uzytkownik):
        self._fasada_encji = fasada_encji
        self._uzytkownik = uzytkownik

    def wykonaj(self):
        if not self._uzytkownik:
            print("Błąd: Musisz być zalogowany, aby złożyć zamówienie.")
            return

        print(f"ProcesSkladaniaZamowienia: Przetwarzam zamówienie dla {self._uzytkownik.login}...")
        raise NotImplementedError("PU: Składanie zamówienia niezaimplementowane.")