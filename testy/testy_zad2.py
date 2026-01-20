import unittest
from unittest.mock import MagicMock, patch, call
from typing import List

from encje.Administrator import Administrator
from kontrola.KsiegarniaKontrolaFacade import KsiegarniaKontrolaFacade
from encje.IEncjeFasada import IEncjeFasada
from encje.Klient import Klient
from encje.IKsiazka import IKsiazka


def tag(*tags):
    def decorator(func):
        func.tags = set(tags)
        return func

    return decorator


class TestKsiegarniaKontrolaMock(unittest.TestCase):

    def setUp(self):
        # 1. Atrapa bazy danych
        self.mock_encje = MagicMock(spec=IEncjeFasada)
        self.facade = KsiegarniaKontrolaFacade(self.mock_encje)

        # 2. Atrapa kontekstu logowania
        self.facade._kontekst_auth = MagicMock()

        # 3. Atrapa Administratora
        self.admin = MagicMock(spec=Administrator)
        self.facade._kontekst_auth.getZalogowanyUzytkownik.return_value = self.admin

    @tag("kontrola", "krytyczne")
    @patch('kontrola.KsiegarniaKontrolaFacade.ProcesSkladaniaZamowienia')
    def test_zlozZamowienie_pelny_przeplyw(self, MockProces):
        # GIVEN
        mock_user = MagicMock(spec=Klient)
        self.facade._kontekst_auth.getZalogowanyUzytkownik.return_value = mock_user
        lista_isbn = [123, 456]

        # WHEN
        self.facade.zlozZamowienie(id_klienta=1, lista_ISBN=lista_isbn)

        # THEN
        #Sprawdzanie czy pobrano uzytkownika
        self.facade._kontekst_auth.getZalogowanyUzytkownik.assert_called_once()

        #Czy fasada wywolala metode w procesie
        MockProces.return_value.wykonajSkladanieZamowienia.assert_called_with(1, lista_isbn)


    # WERYFIKACJA INTERAKCJI I KOLEJNOŚCI

    @tag("kontrola", "kolejnosc")
    def test_zalogujKlienta_kolejnosc_strategii(self):
        """Weryfikacja kolejności: najpierw ustawienie strategii, potem login."""
        self.facade.zalogujKlienta("haslo", "test@test.pl")

        # Sprawdzamy kolejność wywołań na mocku kontekstu
        oczekiwane = [
            call.ustawStrategie(self.facade._strategia_klienta),
            call.wykonajUwierzytelnianie("test@test.pl", "haslo")
        ]
        self.facade._kontekst_auth.assert_has_calls(oczekiwane, any_order=False)

    @tag("kontrola", "mock")
    def test_wybierzKsiazke_wyswietla_komunikat(self):
        mock_k = MagicMock(spec=IKsiazka)
        mock_k.id = 10;
        mock_k.tytul = "Ksiazka1";
        mock_k.autor = "Autor Autor";
        mock_k.cena = 40.0
        self.mock_encje.pobierzPoISBN.return_value = mock_k

        with patch('builtins.print') as mock_print:
            self.facade.wybierzKsiazke(ISBN=1234567890123)
            mock_print.assert_called_with("Wybrano książkę: [10] Ksiazka1 – Autor Autor – 40.0 zł")

    @tag("kontrola", "mock")
    def test_wybierzKsiazke_brak_ksiazki(self):
        """Testuje scenariusz, gdy książka nie istnieje w bazie."""
        self.mock_encje.pobierzPoISBN.return_value = None

        with patch('builtins.print') as mock_print:
            self.facade.wybierzKsiazke(ISBN=1234567890123)
            mock_print.assert_called_with("Nie znaleziono książki o ISBN: 1234567890123")

    @tag("kontrola", "mock")
    @patch('kontrola.KsiegarniaKontrolaFacade.ZarzadzanieKsiazkami')
    def test_zarzadzajKatalogiem_pobiera_uzytkownika(self, MockProces):
        """
   Czy podczas zarzadzania katalogiem weryfikujemy czy uzytkownik jest administratorem
        """
        # WHEN
        self.facade.zarzadzajKatalogiem()

        # THEN
        self.facade._kontekst_auth.getZalogowanyUzytkownik.assert_called_once()
        MockProces.return_value.zarzadzajKsiazkami.assert_called_once()

    @tag("kontrola", "podstawowe")
    @patch('kontrola.KsiegarniaKontrolaFacade.ProcesPrzegladaniaHistorii')
    def test_przegladajHistorie_wywolanie_procesu(self, MockProces):
        self.facade.przegladajHistorie(id_klienta=5)
        self.facade._kontekst_auth.getZalogowanyUzytkownik.assert_called()
        MockProces.return_value.wykonajPrzegladanieHistorii.assert_called_with(5)

    @tag("kontrola", "bezpieczenstwo")
    def test_wylogujUzytkownika_czysci_kontekst(self):
        self.facade.wylogujUzytkownika()
        self.facade._kontekst_auth.wyloguj.assert_called_once()

    @tag("kontrola", "raporty")
    @patch('kontrola.KsiegarniaKontrolaFacade.ProcesPrzegladaniaRaportu')
    def test_przegladajRaporty_wymaga_autoryzacji(self, MockProces):
        self.facade.przegladajRaporty()
        self.facade._kontekst_auth.getZalogowanyUzytkownik.assert_called()
        MockProces.return_value.wykonajPrzegladanieRaportu.assert_called_once()


if __name__ == "__main__":
    unittest.main()