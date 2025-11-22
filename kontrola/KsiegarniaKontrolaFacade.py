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
    def __init__(self, fasada_encji: IEncjeFasada):
        self._fasada_encji = fasada_encji
        self._strategia_klienta = StrategiaLogowanieKlienta(fasada_encji)
        self._strategia_admina = StrategiaLogowanieAdministratora(fasada_encji)
        self._kontekst_auth = KontekstUwierzytelniania()

    def stworzKonto(self):
        proces = ProcesRejestracji(self.encje_fasada)
        proces.wykonaj()

    def zalogujKlienta(self):
        strategia = StrategiaLogowanieKlienta(self.encje_fasada)
        self.kontekst_auth.ustawStrategie(strategia)
        # Hardcoded dane dla przykładu
        self.kontekst_auth.wykonajUwierzytelnianie("klient@test.pl", "haslo123")

    def zalogujAdministratora(self):
        strategia = StrategiaLogowanieAdministratora(self.encje_fasada)
        self.kontekst_auth.ustawStrategie(strategia)
        self.kontekst_auth.wykonajUwierzytelnianie("admin@test.pl", "admin123")

    def zarzadzajKatalogiem(self):
        user = self.kontekst_auth.getZalogowanyUzytkownik()
        proces = ZarzadzanieKsiazkami(self.encje_fasada, user)
        proces.wykonajZarzadzanie()

    def zarzadzajUzytkownikami(self):
        user = self.kontekst_auth.getZalogowanyUzytkownik()
        proces = ZarzadzanieUzytkownikami(self.encje_fasada, user)
        proces.wykonajZarzadzanie()

    def przegladajKsiazki(self):
        proces = ProcesPrzegladaniaKsiazek(self.encje_fasada)
        proces.wykonaj()

    def zlozZamowienie(self):
        user = self.kontekst_auth.getZalogowanyUzytkownik()
        proces = ProcesSkladaniaZamowienia(self.encje_fasada, user)
        proces.wykonaj()

    # Implementacja pozostałych metod z interfejsu (puste dla zwięzłości)
    def przegladajRaporty(self):
        proces = ProcesPrzegladaniaRaportu(self.encje_fasada)
        proces.wykonaj()

    def usunKonto(self):
        proces = ProcesUsuwaniaKonta(self.encje_fasada)
        proces.wykonaj()

    def wybierzKsiazke(self):
        pass

    def przegladajHistorie(self):
        proces = ProcesPrzegladaniaHistorii(self.encje_fasada)
        proces.wykonaj()