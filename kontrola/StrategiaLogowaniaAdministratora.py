from kontrola.IStrategiaUwierzytelniania import IStrategiaUwierzytelniania
from encje.IEncjeFasada import IEncjeFasada
from encje.Uzytkownik import Uzytkownik
from typing import Optional
import hashlib  # jeśli porównywać hashe


class StrategiaLogowanieAdministratora(IStrategiaUwierzytelniania):
    def __init__(self, fasada_encji: IEncjeFasada):
        self._fasada_encji = fasada_encji

    def uwierzytelnij(self, login: str, haslo: str) -> Optional[Uzytkownik]:
        print("StrategiaAdmin: Weryfikacja uprawnień admina...")
        # 1. Pobierz użytkownika po loginie
        uzytkownik = self._fasada_encji.znajdzUzytkownikaPoLoginie(login)

        # 2. Sprawdzenie czy istnieje
        if not uzytkownik:
            print("StrategiaAdmin: użytkownik nie istnieje.")
            return None

        # 3. Sprawdzenie roli

        # 4. Sprawdzenie hasła - czy hashujemy haslo??
        # Jeśli hash nie jest używany, po prostu: if uzytkownik.haslo != haslo:
        if uzytkownik.hashHasla != haslo:
            print("StrategiaAdmin: niepoprawne hasło.")
            return None

        if uzytkownik:
            return uzytkownik
        return None




