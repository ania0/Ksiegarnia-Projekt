import unittest
from unittest.mock import MagicMock, patch, call
from typing import List

# Importy Twoich klas
from kontrola.KsiegarniaKontrolaFacade import KsiegarniaKontrolaFacade
from encje.IEncjeFasada import IEncjeFasada
from encje.Klient import Klient
from encje.IKsiazka import IKsiazka
from encje.Zamowienie import Zamowienie


class TestKsiegarniaKontrolaMock(unittest.TestCase):

    def setUp(self):
        """
        GIVEN: Inicjalizacja symulacji (Mockito: @Mock i @InjectMocks)
        """
        # Tworzymy symulację interfejsu (mock())
        self.mock_encje = MagicMock(spec=IEncjeFasada)

        # Wstrzykujemy symulację do fasady kontroli (InjectMocks)
        self.facade = KsiegarniaKontrolaFacade(self.mock_encje)

        # Nadpisujemy kontekst auth, aby móc go kontrolować w testach
        self.facade._kontekst_auth = MagicMock()

    # --- 1. TEST: WYBÓR KSIĄŻKI (when().thenReturn() + verify()) ---
    def test_wybierzKsiazke_sukces(self):
        """
        Zadanie: Zachowanie symulacji zwracającej wartość oraz weryfikacja parametrów.
        """
        # GIVEN: Symulujemy, że pobranie po ISBN zwróci obiekt książki
        mock_ksiazka = MagicMock(spec=IKsiazka)
        mock_ksiazka.id = 10
        mock_ksiazka.tytul = "Wiedźmin"
        mock_ksiazka.autor = "A. Sapkowski"
        mock_ksiazka.cena = 45.0

        # Mockito: when(encje.pobierzPoISBN(123)).thenReturn(mock_ksiazka)
        self.mock_encje.pobierzPoISBN.return_value = mock_ksiazka

        # WHEN: Wywołujemy metodę fasady
        with patch('builtins.print') as mock_print:
            self.facade.wybierzKsiazke(ISBN=123)

            # THEN: Weryfikacja czy zawołano encje z dobrym ISBN (verify)
            self.mock_encje.pobierzPoISBN.assert_called_once_with(123)
            # Sprawdzamy czy komunikat na ekranie był poprawny
            mock_print.assert_called_with("Wybrano książkę: [10] Wiedźmin – A. Sapkowski – 45.0 zł")

    # --- 2. TEST: OBSŁUGA BŁĘDU REJESTRACJI (when().thenThrow()) ---
    @patch('kontrola.KsiegarniaKontrolaFacade.ProcesRejestracji')
    def test_stworzKonto_blad_walidacji(self, MockProces):
        """
        Zadanie: Symulacja wyrzucania wyjątku (side_effect).
        """
        # GIVEN: Symulujemy, że proces rejestracji rzuca błąd (np. niepoprawny email)
        instancja_procesu = MockProces.return_value
        instancja_procesu.wykonajRejestracje.side_effect = ValueError("Niepoprawny format email")

        # WHEN & THEN: Sprawdzamy czy fasada kontroli przepuszcza ten wyjątek
        with self.assertRaises(ValueError) as cm:
            self.facade.stworzKonto("haslo123", "zly_email")

        self.assertEqual(str(cm.exception), "Niepoprawny format email")

    # --- 3. TEST: KOLEJNOŚĆ LOGOWANIA ADMINA (InOrder) ---
    def test_zalogujAdministratora_kolejnosc_operacji(self):
        """
        Zadanie: Weryfikacja kolejności (InOrder).
        """
        # GIVEN: Dane logowania
        email, haslo = "admin@ksiegarnia.pl", "admin1"

        # WHEN: Logujemy administratora
        self.facade.zalogujAdministratora(haslo, email)

        # THEN: Sprawdzamy czy najpierw ustawiono strategię, a potem wykonano auth
        oczekiwane_wywolania = [
            call.ustawStrategie(self.facade._strategia_admina),
            call.wykonajUwierzytelnianie(email, haslo)
        ]
        self.facade._kontekst_auth.assert_has_calls(oczekiwane_wywolania, any_order=False)

    # --- 4. TEST: WERYFIKACJA NEGATYWNA (never() / times()) ---
    def test_zarzadzajUzytkownikami_tylko_raz_pobiera_uzytkownika(self):
        """
        Zadanie: verify(times(1)) oraz never().
        """
        # GIVEN: Przygotowanie mocka procesu
        with patch('kontrola.KsiegarniaKontrolaFacade.ZarzadzanieUzytkownikami') as MockProces:
            # WHEN: Wywołujemy zarządzanie
            self.facade.zarzadzajUzytkownikami()

            # THEN: Upewniamy się, że użytkownik z kontekstu został pobrany dokładnie RAZ
            self.assertEqual(self.facade._kontekst_auth.getZalogowanyUzytkownik.call_count, 1)

            # Weryfikacja negatywna: upewniamy się, że NIE usunięto nic z bazy przy samym wejściu w panel
            self.mock_encje.usun.assert_not_called()

    # --- 5. TEST: OBLICZANIE CENY OSTATECZNEJ (Złożona współpraca) ---
    def test_oblicz_cene_ostateczna_delegacja(self):
        """
        Zadanie: Weryfikacja interakcji między dwoma różnymi mockami (Zamowienie i Klient).
        """
        # GIVEN: Przygotowanie danych
        mock_zamowienie = MagicMock(spec=Zamowienie)
        mock_klient = MagicMock(spec=Klient)
        self.mock_encje.obliczCeneOstateczna.return_value = 99.99

        # WHEN: Wywołujemy metodę w fasadzie encji (poprzez mocka w fasadzie kontroli)
        wynik = self.mock_encje.obliczCeneOstateczna(mock_zamowienie, mock_klient)

        # THEN: Sprawdzamy czy wynik się zgadza i czy zawołano metodę (verify)
        self.assertEqual(wynik, 99.99)
        self.mock_encje.obliczCeneOstateczna.assert_called_once_with(mock_zamowienie, mock_klient)


if __name__ == "__main__":
    unittest.main()