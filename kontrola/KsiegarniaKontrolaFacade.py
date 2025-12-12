from typing import Optional, List
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
        proces = ProcesRejestracji(self._encje_fasada)
        proces.wykonajRejestracje(email, haslo)

    def zalogujKlienta(self, haslo: str, email: str):
        self._kontekst_auth.ustawStrategie(self._strategia_klienta)
        return self._kontekst_auth.wykonajUwierzytelnianie(email, haslo)

    def zalogujAdministratora(self, haslo: str, email: str):
        self._kontekst_auth.ustawStrategie(self._strategia_admina)
        return self._kontekst_auth.wykonajUwierzytelnianie(email, haslo)

    def zarzadzajKatalogiem(self) -> None:
        uzytkownik = self._kontekst_auth.getZalogowanyUzytkownik()
        proces = ZarzadzanieKsiazkami(self._encje_fasada, uzytkownik)
        proces.zarzadzajKsiazkami()

    def zarzadzajUzytkownikami(self) -> None:
        uzytkownik = self._kontekst_auth.getZalogowanyUzytkownik()
        proces = ZarzadzanieUzytkownikami(self._encje_fasada, uzytkownik)
        proces.zarzadzajUzytkownikami()

    def przegladajKsiazki(self) -> None:
        proces = ProcesPrzegladaniaKsiazek(self._encje_fasada)
        proces.wykonajPrzegladanieKsiazek()

    def przegladajRaporty(self) -> None:
        uzytkownik = self._kontekst_auth.getZalogowanyUzytkownik()
        proces = ProcesPrzegladaniaRaportu(self._encje_fasada, uzytkownik)
        proces.wykonajPrzegladanieRaportu()

    def wybierzKsiazke(self, ISBN: int) -> None:
        ksiazka = self._encje_fasada.pobierzPoISBN(ISBN)
        # CZY TAK MOŻE BYĆ?
        if ksiazka:
            print(f"Wybrano książkę: [{ksiazka.id}] {ksiazka.tytul} – {ksiazka.autor} – {ksiazka.cena} zł")
        else:
            print(f"Nie znaleziono książki o ISBN: {ISBN}")

    def zlozZamowienie(self, id_klienta: int, lista_ISBN: List[int]) -> None:
        uzytkownik = self._kontekst_auth.getZalogowanyUzytkownik()
        proces = ProcesSkladaniaZamowienia(self._encje_fasada, uzytkownik)
        proces.wykonajSkladanieZamowienia(id_klienta, lista_ISBN)

    def przegladajHistorie(self, id_klienta: int) -> None:
        uzytkownik = self._kontekst_auth.getZalogowanyUzytkownik()
        proces = ProcesPrzegladaniaHistorii(self._encje_fasada, uzytkownik)
        proces.wykonajPrzegladanieHistorii(id_klienta)

    def usunKonto(self, id_klienta: int) -> None:
        # Przekazujemy stub użytkownika lub ID do procesu
        uzytkownik = self._kontekst_auth.getZalogowanyUzytkownik()
        proces = ProcesUsuwaniaKonta(self._encje_fasada, uzytkownik)
        proces.wykonajUsuwanie(id_klienta)

    def wylogujUzytkownika(self) -> None:
        """
        Wylogowuje użytkownika poprzez wyczyszczenie kontekstu uwierzytelniania.
        """
        self._kontekst_auth.wyloguj()