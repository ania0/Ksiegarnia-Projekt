from .istrategia_uwierzytelniania import IStrategiaUwierzytelniania


class KontekstUwierzytelniania:
    # Asocjacja - Kontekst "posiada" strategię
    def __init__(self, strategia: IStrategiaUwierzytelniania):
        self._strategia = strategia

    def ustawStrategie(self, strategia: IStrategiaUwierzytelniania):
        self._strategia = strategia

    def wykonaj_uwierzytelnienie(self, login, haslo):
        return self._strategia.uwierzytelnij(login, haslo)