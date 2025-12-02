from typing import Optional, List

# TU

from kontrola.IKsiegarniaKontrola import IKsiegarniaKontrola
from encje.IEncjeFasada import IEncjeFasada

from kontrola.KontekstUwierzytelniania import KontekstUwierzytelniania
from kontrola.StrategiaLogowaniaKlienta import StrategiaLogowanieKlienta
from kontrola.StrategiaLogowaniaAdministratora import StrategiaLogowanieAdministratora

# Importy Procesów
from kontrola.ProcesRejestracji import ProcesRejestracji
from kontrola.ProcesPrzegladaniaKsiazek import ProcesPrzegladaniaKsiazek
from kontrola.ProcesPrzegladaniaHistorii import ProcesPrzegladaniaHistorii
from kontrola.ProcesPrzegladaniaRaportu import ProcesPrzegladaniaRaportu
from kontrola.ProcesSkladaniaZamowienia import ProcesSkladaniaZamowienia
from kontrola.ProcesUsuwaniaKonta import ProcesUsuwaniaKonta
from kontrola.ZarzadzanieKsiazkami import ZarzadzanieKsiazkami
from kontrola.ZarzadzanieUzytkownikami import ZarzadzanieUzytkownikami


class KsiegarniaKontrolaFacade(IKsiegarniaKontrola):
    """
    Fasada warstwy kontroli – realizuje przypadki użycia.
    """
    def __init__(self, encje_fasada: IEncjeFasada):
        self._encje_fasada: IEncjeFasada = encje_fasada

        self._kontekst_auth = KontekstUwierzytelniania()
        self._strategia_klienta = StrategiaLogowanieKlienta(encje_fasada)
        self._strategia_admina = StrategiaLogowanieAdministratora(encje_fasada)

    def stworzKonto(self, haslo: str, email: str) -> None:
        proces = ProcesRejestracji()
        proces.wykonajRejestracje(email, haslo)


    def zalogujKlienta(self, hashHasla: str, email: str) -> None:
        self._kontekst_auth.ustawStrategie(self._strategia_klienta)
        self._kontekst_auth.wykonajUwierzytelnianie(email, hashHasla)

    def zalogujAdministratora(self, hashHasla: str, email: str) -> None:
        self._kontekst_auth.ustawStrategie(self._strategia_admina)
        self._kontekst_auth.wykonajUwierzytelnianie(email, hashHasla)

    def zarzadzajKatalogiem(self, polecenie=None) -> None:
        uzytkownik = self._kontekst_auth.getZalogowanyUzytkownik()
        proces = ZarzadzanieKsiazkami(self._encje_fasada, uzytkownik)
        proces.zarzadzajKsiazkami(polecenie)

    def zarzadzajUzytkownikami(self) -> None:
        uzytkownik = self._kontekst_auth.getZalogowanyUzytkownik()
        proces = ZarzadzanieUzytkownikami(self._encje_fasada, uzytkownik)
        proces.zarzadzajUzytkownikami()

    def przegladajKsiazki(self) -> None:
        proces = ProcesPrzegladaniaKsiazek(self._encje_fasada)
        proces.wykonajPrzegladanieKsiazek()

    def przegladajRaporty(self) -> None:
        proces = ProcesPrzegladaniaRaportu(self._encje_fasada)
        proces.wykonajPrzegladanieRaportu()

    def wybierzKsiazke(self, ISBN: int) -> None:
        return None

    def zlozZamowienie(self, id_klienta: int, lista_id_ksiazek: List[int]) -> None:
        uzytkownik = self._kontekst_auth.getZalogowanyUzytkownik()
        proces = ProcesSkladaniaZamowienia(self._encje_fasada, uzytkownik)
        proces.wykonajSkladanieZamowienia(id_klienta, lista_id_ksiazek)

    def przegladajHistorie(self, id_klienta: int) -> None:
        uzytkownik = self._kontekst_auth.getZalogowanyUzytkownik()
        proces = ProcesPrzegladaniaHistorii(self._encje_fasada, uzytkownik)
        proces.wykonajPrzegladanieHistorii(id_klienta)

    def usunKonto(self, id_klienta: int) -> None:
        # Przekazujemy stub użytkownika lub ID do procesu
        proces = ProcesUsuwaniaKonta(self._encje_fasada)
        proces.wykonajUsuwanie(id_klienta)