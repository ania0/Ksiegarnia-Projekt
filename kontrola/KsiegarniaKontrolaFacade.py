from kontrola.IKsiegarniaKontrola import IKsiegarniaKontrola
from encje.IEncjeFasada import IEncjeFasada

from kontrola.KontekstUwierzytelniania import KontekstUwierzytelniania
from kontrola.StrategiaLogowaniaKlienta import StrategiaLogowanieKlienta
from kontrola.StrategiaLogowaniaAdministratora import StrategiaLogowanieAdministratora

from kontrola.ProcesRejestracji import ProcesRejestracji
from kontrola.ProcesSkladaniaZamowienia import ProcesSkladaniaZamowienia
from kontrola.ProcesPrzegladaniaKsiazek import ProcesPrzegladaniaKsiazek
from kontrola.ZarzadzanieKsiazkami import ZarzadzanieKsiazkami
from kontrola.ZarzadzanieUzytkownikami import ZarzadzanieUzytkownikami
from kontrola.ProcesPrzegladaniaHistorii import ProcesPrzegladaniaHistorii
from kontrola.ProcesPrzegladaniaRaportu import ProcesPrzegladaniaRaportu
from kontrola.ProcesUsuwaniaKonta import ProcesUsuwaniaKonta

class KsiegarniaKontrolaFacade(IKsiegarniaKontrola):
    def __init__(self, encje_fasada: IEncjeFasada):
        # Pola prywatne zazwyczaj mają podkreślnik na początku
        self._encje_fasada = encje_fasada
        self._strategia_klienta = StrategiaLogowanieKlienta(encje_fasada)
        self._strategia_admina = StrategiaLogowanieAdministratora(encje_fasada)
        self._kontekst_auth = KontekstUwierzytelniania()

    # --- POPRAWKA 1: Dodano argument 'dane' ---
    def stworzKonto(self, dane):
        # --- POPRAWKA 2: Używamy self._encje_fasada (z podkreślnikiem) ---
        proces = ProcesRejestracji(self._encje_fasada)
        proces.wykonaj()

    # --- POPRAWKA 1: Dodano 'login' i 'haslo' ---
    def zalogujKlienta(self, login, haslo):
        strategia = StrategiaLogowanieKlienta(self._encje_fasada)
        # --- POPRAWKA 2: Używamy self._kontekst_auth (z podkreślnikiem) ---
        self._kontekst_auth.ustawStrategie(strategia)
        return self._kontekst_auth.wykonajUwierzytelnianie(login, haslo)

    # --- POPRAWKA 1: Dodano 'login' i 'haslo' ---
    def zalogujAdministratora(self, login, haslo):
        strategia = StrategiaLogowanieAdministratora(self._encje_fasada)
        self._kontekst_auth.ustawStrategie(strategia)
        return self._kontekst_auth.wykonajUwierzytelnianie(login, haslo)

    # --- POPRAWKA 1: Dodano parametr opcjonalny 'polecenie' ---
    def zarzadzajKatalogiem(self, polecenie=None):
        user = self._kontekst_auth.getZalogowanyUzytkownik()
        proces = ZarzadzanieKsiazkami(self._encje_fasada, user)
        proces.wykonajZarzadzanie()

    def zarzadzajUzytkownikami(self):
        user = self._kontekst_auth.getZalogowanyUzytkownik()
        proces = ZarzadzanieUzytkownikami(self._encje_fasada, user)
        proces.wykonajZarzadzanie()

    def przegladajKsiazki(self):
        proces = ProcesPrzegladaniaKsiazek(self._encje_fasada)
        proces.wykonaj()

    # --- POPRAWKA 1: Dodano 'koszyk' ---
    def zlozZamowienie(self, koszyk):
        user = self._kontekst_auth.getZalogowanyUzytkownik()
        proces = ProcesSkladaniaZamowienia(self._encje_fasada, user)
        proces.wykonaj()

    def przegladajRaporty(self):
        proces = ProcesPrzegladaniaRaportu(self._encje_fasada)
        proces.wykonaj()

    def usunKonto(self):
        proces = ProcesUsuwaniaKonta(self._encje_fasada)
        proces.wykonaj()

    # --- POPRAWKA 1: Dodano 'id' ---
    def wybierzKsiazke(self, id):
        pass

    def przegladajHistorie(self):
        proces = ProcesPrzegladaniaHistorii(self._encje_fasada)
        proces.wykonaj()