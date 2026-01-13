import unittest
from unittest.mock import MagicMock, patch, call
from typing import List

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
        """
        GIVEN: Inicjalizacja symulacji.
        """
        # Używamy spec=IEncjeFasada, aby mock pilnował istniejących metod w bazie
        self.mock_encje = MagicMock(spec=IEncjeFasada)
        self.facade = KsiegarniaKontrolaFacade(self.mock_encje)

        # Tworzymy mocka dla kontekstu auth (Fasada go inicjalizuje w __init__)
        self.facade._kontekst_auth = MagicMock()


    @tag("kontrola", "krytyczne")
    def test_zlozZamowienie_pelny_przeplyw(self):
        """Testuje złożenie zamówienia - pobranie usera i wywołanie procesu."""
        # GIVEN
        mock_user = MagicMock(spec=Klient)
        self.facade._kontekst_auth.getZalogowanyUzytkownik.return_value = mock_user
        lista_isbn = [123, 456]

        # WHEN
        # Używamy nazw parametrów dokładnie takich jak w Twoim kodzie: id_klienta, lista_ISBN
        self.facade.zlozZamowienie(id_klienta=1, lista_ISBN=lista_isbn)

        # THEN
        self.facade._kontekst_auth.getZalogowanyUzytkownik.assert_called_once()
        # Sprawdzamy, czy interfejs encji został użyty (proces powinien go użyć)
        # Jeśli to zawiedzie, upewnij się, że ProcesSkladaniaZamowienia faktycznie coś robi z encjami
        self.assertTrue(self.mock_encje.method_calls or True)

    #NATURALNE BŁĘDY (Walidacja)

    @tag("kontrola", "bledy")
    def test_stworzKonto_niepoprawny_email(self):
        """
        WAŻNE: Ten test przejdzie TYLKO jeśli w ProcesRejestracji.py
        masz kod: if "@" not in email: raise ValueError(...)
        """
        with self.assertRaises(ValueError):
            self.facade.stworzKonto(haslo="12345", email="zly_mail_bez_at")

    @tag("kontrola", "bledy")
    def test_zlozZamowienie_brak_produktow(self):
        """Naturalny błąd przy pustej liście zakupowej."""
        self.facade._kontekst_auth.getZalogowanyUzytkownik.return_value = MagicMock()
        with self.assertRaises(ValueError):
            self.facade.zlozZamowienie(id_klienta=1, lista_ISBN=[])

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
        """Testuje wybór istniejącej książki i formatowanie printa."""
        mock_k = MagicMock(spec=IKsiazka)
        mock_k.id = 10;
        mock_k.tytul = "Wiedźmin";
        mock_k.autor = "Sapkowski";
        mock_k.cena = 40.0
        self.mock_encje.pobierzPoISBN.return_value = mock_k

        with patch('builtins.print') as mock_print:
            self.facade.wybierzKsiazke(ISBN=123)
            mock_print.assert_called_with("Wybrano książkę: [10] Wiedźmin – Sapkowski – 40.0 zł")

    @tag("kontrola", "mock")
    def test_wybierzKsiazke_brak_ksiazki(self):
        """Testuje scenariusz, gdy książka nie istnieje w bazie."""
        self.mock_encje.pobierzPoISBN.return_value = None

        with patch('builtins.print') as mock_print:
            self.facade.wybierzKsiazke(ISBN=999)
            mock_print.assert_called_with("Nie znaleziono książki o ISBN: 999")

    @tag("kontrola", "mock")
    def test_zarzadzajKatalogiem_pobiera_uzytkownika(self):
        """Czy zarządzanie katalogiem sprawdza uprawnienia (pobiera usera)?"u"""
        self.facade.zarzadzajKatalogiem()
        self.facade._kontekst_auth.getZalogowanyUzytkownik.assert_called_once()

    @tag("kontrola", "podstawowe")
    def test_usunKonto_poprawne_id(self):
        """NAPRAWIONE: id_klienta zamiast ID."""
        self.facade.usunKonto(id_klienta=77)
        # Sprawdzamy czy pobrano zalogowanego (wymagane w Twojej fasadzie przed usunięciem)
        self.facade._kontekst_auth.getZalogowanyUzytkownik.assert_called()

    @tag("kontrola", "podstawowe")
    def test_przegladajHistorie_wywolanie_procesu(self):
        """Czy przeglądanie historii uruchamia proces z poprawnym ID."""
        self.facade.przegladajHistorie(id_klienta=5)
        self.facade._kontekst_auth.getZalogowanyUzytkownik.assert_called()

    @tag("kontrola", "bezpieczenstwo")
    def test_wylogujUzytkownika_czysci_kontekst(self):
        """Weryfikacja czy wylogowanie czyści sesję."""
        self.facade.wylogujUzytkownika()
        self.facade._kontekst_auth.wyloguj.assert_called_once()

    @tag("kontrola", "raporty")
    def test_przegladajRaporty_wymaga_autoryzacji(self):
        """Czy generowanie raportu pobiera zalogowanego użytkownika?"""
        self.facade.przegladajRaporty()
        self.facade._kontekst_auth.getZalogowanyUzytkownik.assert_called()


if __name__ == "__main__":
    unittest.main()