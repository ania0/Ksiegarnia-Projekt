# from kontrola.IKsiegarniaKontrola import IKsiegarniaKontrola
# from encje.IEncjeFasada import IEncjeFasada
#
# from kontrola.KontekstUwierzytelniania import KontekstUwierzytelniania
# from kontrola.StrategiaLogowaniaKlienta import StrategiaLogowanieKlienta
# from kontrola.StrategiaLogowaniaAdministratora import StrategiaLogowanieAdministratora
#
# from kontrola.ProcesRejestracji import ProcesRejestracji
# from kontrola.ProcesSkladaniaZamowienia import ProcesSkladaniaZamowienia
# from kontrola.ProcesPrzegladaniaKsiazek import ProcesPrzegladaniaKsiazek
# from kontrola.ZarzadzanieKsiazkami import ZarzadzanieKsiazkami
# from kontrola.ZarzadzanieUzytkownikami import ZarzadzanieUzytkownikami
# from kontrola.ProcesPrzegladaniaHistorii import ProcesPrzegladaniaHistorii
# from kontrola.ProcesPrzegladaniaRaportu import ProcesPrzegladaniaRaportu
# from kontrola.ProcesUsuwaniaKonta import ProcesUsuwaniaKonta
#
# class KsiegarniaKontrolaFacade(IKsiegarniaKontrola):
#     def __init__(self, encje_fasada: IEncjeFasada):
#         self._encje_fasada = encje_fasada
#         self._strategia_klienta = StrategiaLogowanieKlienta(encje_fasada)
#         self._strategia_admina = StrategiaLogowanieAdministratora(encje_fasada)
#         self._kontekst_auth = KontekstUwierzytelniania()
#
#     def stworzKonto(self, dane):
#         proces = ProcesRejestracji(self._encje_fasada)
#         proces.wykonaj()
#
#     def zalogujKlienta(self, login, haslo):
#         strategia = StrategiaLogowanieKlienta(self._encje_fasada)
#         self._kontekst_auth.ustawStrategie(strategia)
#         return self._kontekst_auth.wykonajUwierzytelnianie(login, haslo)
#
#     def zalogujAdministratora(self, login, haslo):
#         strategia = StrategiaLogowanieAdministratora(self._encje_fasada)
#         self._kontekst_auth.ustawStrategie(strategia)
#         return self._kontekst_auth.wykonajUwierzytelnianie(login, haslo)
#
#     def zarzadzajKatalogiem(self, polecenie=None):
#         user = self._kontekst_auth.getZalogowanyUzytkownik()
#         proces = ZarzadzanieKsiazkami(self._encje_fasada, user)
#         proces.wykonajZarzadzanie()
#
#     # def zarzadzajUzytkownikami(self):
#     #     user = self._kontekst_auth.getZalogowanyUzytkownik()
#     #     proces = ZarzadzanieUzytkownikami(self._encje_fasada, user)
#     #     proces.wykonajZarzadzanie()
#
#     def przegladajKsiazki(self):
#         proces = ProcesPrzegladaniaKsiazek(self._encje_fasada)
#         proces.wykonaj()
#
#     # def zlozZamowienie(self, koszyk):
#     #     user = self._kontekst_auth.getZalogowanyUzytkownik()
#     #     proces = ProcesSkladaniaZamowienia(self._encje_fasada, user)
#     #     proces.wykonaj()
#
#     def przegladajRaporty(self):
#         proces = ProcesPrzegladaniaRaportu(self._encje_fasada)
#         proces.wykonaj()
#
#     # def usunKonto(self):
#     #     proces = ProcesUsuwaniaKonta(self._encje_fasada)
#     #     proces.wykonaj()
#
#     def wybierzKsiazke(self, id):
#         pass
#
#     def przegladajHistorie(self):
#         proces = ProcesPrzegladaniaHistorii(self._encje_fasada)
#         proces.wykonaj()
#
#

from typing import Optional

from kontrola.IKsiegarniaKontrola import IKsiegarniaKontrola
from encje.IEncjeFasada import IEncjeFasada

from kontrola.KontekstUwierzytelniania import KontekstUwierzytelniania
from kontrola.StrategiaLogowaniaKlienta import StrategiaLogowanieKlienta
from kontrola.StrategiaLogowaniaAdministratora import StrategiaLogowanieAdministratora

from kontrola.ProcesRejestracji import ProcesRejestracji
from kontrola.ProcesPrzegladaniaKsiazek import ProcesPrzegladaniaKsiazek
from kontrola.ProcesPrzegladaniaHistorii import ProcesPrzegladaniaHistorii
from kontrola.ProcesPrzegladaniaRaportu import ProcesPrzegladaniaRaportu
from kontrola.ZarzadzanieKsiazkami import ZarzadzanieKsiazkami


class KsiegarniaKontrolaFacade(IKsiegarniaKontrola):
    """
    Fasada warstwy kontroli – wersja szkieletowa zgodna z wymaganiami laboratoriów.
    Brak implementacji logiki przypadków użycia.
    """

    def __init__(self, encje_fasada: IEncjeFasada):
        # Asocjacja z warstwą encji (fasada encji)
        self._encje_fasada: IEncjeFasada = encje_fasada
        self._strategia_klienta: StrategiaLogowanieKlienta = None
        self._strategia_admina: StrategiaLogowanieAdministratora = None
        self._kontekst_auth: KontekstUwierzytelniania = None


    def stworzKonto(self, dane) -> None:
        raise NotImplementedError("stworzKonto() nie jest jeszcze zaimplementowane.")

    def zalogujKlienta(self, hashHasla: str, email: str) -> None:
        return None  # domyślna wartość

    def zalogujAdministratora(self, hashHasla: str, email: str) -> None:
        return None  # domyślna wartość

    def zarzadzajKatalogiem(self, polecenie=None) -> None: # czy polecenie?
        raise NotImplementedError("zarzadzajKatalogiem() nie jest jeszcze zaimplementowane.")

    def przegladajKsiazki(self) -> None:
        raise NotImplementedError("przegladajKsiazki() nie jest jeszcze zaimplementowane.")

    def przegladajRaporty(self) -> None:
        raise NotImplementedError("przegladajRaporty() nie jest jeszcze zaimplementowane.")

    def wybierzKsiazke(self, ISBN: int) -> None:
        return None  # domyślna wartość

    def przegladajHistorie(self, dane) -> None: #czy tu dane czy id ?
        raise NotImplementedError("przegladajHistorie() nie jest jeszcze zaimplementowane.")

    def usunKonto(self, dane) -> None:
        raise NotImplementedError("usunKonto() nie jest jeszcze zaimplementowane.")

