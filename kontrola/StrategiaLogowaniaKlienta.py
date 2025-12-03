from encje.Klient import Klient
from kontrola.IStrategiaUwierzytelniania import IStrategiaUwierzytelniania
from encje.IEncjeFasada import IEncjeFasada
from encje.Uzytkownik import Uzytkownik
from typing import Optional



class StrategiaLogowanieKlienta(IStrategiaUwierzytelniania):
    def __init__(self, fasada_encji: IEncjeFasada):
        self._fasada_encji = fasada_encji

    def uwierzytelnij(self, email: str, haslo: str) -> Optional[Uzytkownik]:
        # 1. Pobierz użytkownika po emailu
        uzytkownik = self._fasada_encji.znajdzUzytkownikaPoEmailu(email)

        if uzytkownik is not None:
            # 1. SPRAWDZENIE TYPU: Logowanie Klienta powinno działać tylko dla Klientów
            if isinstance(uzytkownik, Klient):
                # 2. WERYFIKACJA HASŁA: Zakładamy, że ta metoda jest poprawna
                if uzytkownik.weryfikujHaslo(haslo):
                    return uzytkownik

        # Zwraca None, jeśli użytkownik nie istnieje lub hasło jest złe
        return None