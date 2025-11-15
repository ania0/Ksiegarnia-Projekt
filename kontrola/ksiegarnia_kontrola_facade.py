from .iksiegarnia_kontrola import IKsiegarniaKontrola
from encje.iencje_fasada import IEncjeFasada

# Importowanie wszystkich "robotników"
from .kontekst_uwierzytelniania import KontekstUwierzytelniania
from .strategia_logowania_klienta import StrategiaLogowaniaKlienta
from .strategia_logowania_administratora import StrategiaLogowaniaAdministratora
from .proces_rejestracji import ProcesRejestracji
from .proces_skladania_zamowienia import ProcesSkladaniaZamowienia
from .proces_usuwania_konta import ProcesUsuwaniaKonta
from .proces_przegladania_raportu import ProcesPrzegladaniaRaportu
from .proces_przegladania_ksiazek import ProcesPrzegladaniaKsiazek
from .proces_przegladania_historii import ProcesPrzegladaniaHistorii


# ... importy reszty procesów ...

# Główna klasa - punkt wejścia do warstwy Kontrola
class KsięgarniaKontrolaFacade(IKsiegarniaKontrola):

    def __init__(self, fasada_encji: IEncjeFasada):
        self._fasada_encji = fasada_encji

        # Inicjalizacja stałych komponentów (z Asocjacji)
        self._strategia_klienta = StrategiaLogowaniaKlienta(fasada_encji)
        self._strategia_admina = StrategiaLogowaniaAdministratora(fasada_encji)
        self._kontekst_uwierzytelniania = KontekstUwierzytelniania(self._strategia_klienta)

        print("KsięgarniaKontrolaFacade: Stworzona i gotowa.")

    # --- Implementacja interfejsu (IKsiegarniaKontrola) ---

    def stworzKonto(self, dane):
        print("FasadaKontroli: Deleguję 'stworzKonto'...")
        # «instantiate» - tworzy obiekt procesu
        proces = ProcesRejestracji(self._fasada_encji)
        return proces.wykonaj(dane)  # i go wywołuje

    def zalogujKlienta(self, login, haslo):
        print("FasadaKontroli: Ustawiam strategię klienta...")
        self._kontekst_uwierzytelniania.ustawStrategie(self._strategia_klienta)
        return self._kontekst_uwierzytelniania.wykonaj_uwierzytelnienie(login, haslo)

    def zalogujAdministratora(self, login, haslo):
        print("FasadaKontroli: Ustawiam strategię admina...")
        self._kontekst_uwierzytelniania.ustawStrategie(self._strategia_admina)
        return self._kontekst_uwierzytelniania.wykonaj_uwierzytelnienie(login, haslo)

    def zlozZamowienie(self, koszyk):
        print("FasadaKontroli: Deleguję 'zlozZamowienie'...")
        proces = ProcesSkladaniaZamowienia(self._fasada_encji)
        return proces.wykonaj(koszyk)

    def usunKonto(self):
        print("FasadaKontroli: Deleguję 'usunKonto'...")
        proces = ProcesUsuwaniaKonta(self._fasada_encji)
        return proces.wykonaj()

    def przegladajRaporty(self):
        print("FasadaKontroli: Deleguję 'przegladajRaporty'...")
        proces = ProcesPrzegladaniaRaportu(self._fasada_encji)
        return proces.wykonaj()

    def przegladajKsiazki(self):
        print("FasadaKontroli: Deleguję 'przegladajKsiazki'...")
        proces = ProcesPrzegladaniaKsiazek(self._fasada_encji)
        return proces.wykonaj()

    def przegladajHistorie(self):
        print("FasadaKontroli: Deleguję 'przegladajHistorie'...")
        proces = ProcesPrzegladaniaHistorii(self._fasada_encji)
        return proces.wykonaj()

    # --- Pozostałe metody to na razie STUBY ---

    def zarzadzajKatalogiem(self, polecenie):
        raise NotImplementedError("PU: zarzadzajKatalogiem nie jest zaimplementowane.")

    def wybierzKsiazke(self, id):
        raise NotImplementedError("PU: wybierzKsiazke nie jest zaimplementowane.")