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
        self._encje_fasada = encje_fasada
        self._strategia_klienta = StrategiaLogowanieKlienta(encje_fasada)
        self._strategia_admina = StrategiaLogowanieAdministratora(encje_fasada)
        self._kontekst_auth = KontekstUwierzytelniania()

    def stworzKonto(self, dane):
        proces = ProcesRejestracji(self._encje_fasada)
        proces.wykonaj()

    def zalogujKlienta(self, login, haslo):
        strategia = StrategiaLogowanieKlienta(self._encje_fasada)
        self._kontekst_auth.ustawStrategie(strategia)
        return self._kontekst_auth.wykonajUwierzytelnianie(login, haslo)

    def zalogujAdministratora(self, login, haslo):
        strategia = StrategiaLogowanieAdministratora(self._encje_fasada)
        self._kontekst_auth.ustawStrategie(strategia)
        return self._kontekst_auth.wykonajUwierzytelnianie(login, haslo)

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

    def wybierzKsiazke(self, id):
        pass

    def przegladajHistorie(self):
        proces = ProcesPrzegladaniaHistorii(self._encje_fasada)
        proces.wykonaj()