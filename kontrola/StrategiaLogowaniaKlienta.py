from kontrola.IStrategiaUwierzytelniania import IStrategiaUwierzytelniania
from encje.IEncjeFasada import IEncjeFasada
from encje.Uzytkownik import Uzytkownik
from typing import Optional
import hashlib  # jeśli porównywać hashe


class StrategiaLogowanieKlienta(IStrategiaUwierzytelniania):
    def __init__(self, fasada_encji: IEncjeFasada):
        self._fasada_encji = fasada_encji

    def uwierzytelnij(self, login: str, haslo: str) -> Optional[Uzytkownik]:
        print("StrategiaKlienta: Weryfikacja w bazie danych...")

        # 1. Pobierz użytkownika po loginie
        uzytkownik = self._fasada_encji.znajdzUzytkownikaPoLoginie(login)

        # 2. Sprawdzenie, czy istnieje
        if not uzytkownik:
            print("StrategiaKlienta: użytkownik nie istnieje.")
            return None

        # 3. Sprawdzenie, że to nie admin (opcjonalnie)

        # 4. Sprawdzenie hasła - czy hashujemy hasło?
        # Jeśli hash nie jest używany, po prostu: if uzytkownik.haslo != haslo:
        if uzytkownik.hashHasla != haslo:
            print("StrategiaKlienta: niepoprawne hasło.")
            return None

        if uzytkownik:
            return uzytkownik
        return None


