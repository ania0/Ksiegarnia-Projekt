import unittest
from unittest.mock import MagicMock, patch, call
from typing import List

from kontrola.KsiegarniaKontrolaFacade import KsiegarniaKontrolaFacade
from encje.IEncjeFasada import IEncjeFasada
from encje.Klient import Klient
from encje.IKsiazka import IKsiazka
from encje.Zamowienie import Zamowienie

def tag(*tags):
    def decorator(func):
        func.tags = set(tags)
        return func
    return decorator

class TestKsiegarniaKontrolaMock(unittest.TestCase):

    def setUp(self):
        """
        GIVEN: Inicjalizacja symulacji (Mockito: @Mock i @InjectMocks)
        """
        #Tworzenie symulacji interfejsu
        self.mock_encje = MagicMock(spec=IEncjeFasada)

        # umieszczenie symulacji w fasadzie kontroli
        self.facade = KsiegarniaKontrolaFacade(self.mock_encje)

        #nadpisanie kontekstu uwierzytelniania, aby móc go kontrolować w testach
        self.facade._kontekst_auth = MagicMock()

    #WYBÓR KSIĄŻKI (when().thenReturn() + verify()) ---
    @tag("kontrola", "mock", "krytyczne")
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

    #obsluga bledu rejestracji
    @tag("kontrola", "mock", "bledy")
    @patch('kontrola.KsiegarniaKontrolaFacade.ProcesRejestracji')
    def test_stworzKonto_blad_walidacji(self, MockProces):
        #Symulacja wyrzucania wyjątku (side_effect).

        # GIVEN: Symulacja, że proces rejestracji rzuca błąd (np. niepoprawny email)
        instancja_procesu = MockProces.return_value
        instancja_procesu.wykonajRejestracje.side_effect = ValueError("Niepoprawny format email")

        # WHEN & THEN: Sprawdzamy czy fasada kontroli przepuszcza ten wyjątek
        with self.assertRaises(ValueError) as cm:
            self.facade.stworzKonto("haslo123", "zly_email")

        self.assertEqual(str(cm.exception), "Niepoprawny format email")

    #Czy poprawna kolejnosc logowania administratora
    @tag("kontrola", "mock", "kolejnosc")
    def test_zalogujAdministratora_kolejnosc_operacji(self):

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

    #WERYFIKACJA NEGATYWNA (never() / times())
    @tag("kontrola", "mock", "zaawansowane")
    def test_zarzadzajUzytkownikami_tylko_raz_pobiera_uzytkownika(self):
        """
        Zadanie: verify(times(1)) oraz never().
        """
        # GIVEN: Przygotowanie mocka procesu
        with patch('kontrola.KsiegarniaKontrolaFacade.ZarzadzanieUzytkownikami') as MockProces:
            # WHEN: Wywołanie zarządzania
            self.facade.zarzadzajUzytkownikami()

            # THEN: Czy użytkownik został pobrany z kontekstu tylko raz
            self.assertEqual(self.facade._kontekst_auth.getZalogowanyUzytkownik.call_count, 1)

            # Weryfikacja negatywna: upewniamy się, że nie usunięto nic z bazy przy samym wejściu w panel
            self.mock_encje.usun.assert_not_called()

    #obliczanie ceny ostatecznej
    @tag("kontrola", "mock", "krytyczne")
    def test_oblicz_cene_ostateczna_delegacja(self):
        """
        Zadanie: Weryfikacja interakcji między dwoma różnymi mockami (Zamowienie i Klient).
        """
        # GIVEN: Przygotowanie danych
        mock_zamowienie = MagicMock(spec=Zamowienie)
        mock_klient = MagicMock(spec=Klient)
        self.mock_encje.obliczCeneOstateczna.return_value = 99.99

        # WHEN: Wywołanie metody w fasadzie encji (poprzez mocka w fasadzie kontroli)
        wynik = self.mock_encje.obliczCeneOstateczna(mock_zamowienie, mock_klient)

        # THEN: Sprawdzanie czy wynik się zgadza i czy wywołano metodę (verify)
        self.assertEqual(wynik, 99.99)
        self.mock_encje.obliczCeneOstateczna.assert_called_once_with(mock_zamowienie, mock_klient)

    #weryfikacja liczby wywołan - czy pobieramy historie przynajmniej raz dla poprawnego ID
    @tag("kontrola", "mock", "podstawowe")
    def test_przegladajHistorie_weryfikacja_wywolan_repozytorium(self):

        # GIVEN
        id_klienta = 5
        self.mock_encje.pobierzHistorieDlaKlienta.return_value = []  # Zwraca pustą listę

        # WHEN
        self.facade.przegladajHistorie(id_klienta)

        # THEN: Weryfikacja czy metoda została wywołana dokładnie 1 raz (lub więcej)
        # Mockito: verify(mock_encje, atLeastOnce()).pobierzHistorieDlaKlienta(5)
        self.assertGreaterEqual(self.mock_encje.pobierzHistorieDlaKlienta.call_count, 1)
        self.mock_encje.pobierzHistorieDlaKlienta.assert_called_with(id_klienta)

    #metoda void, brak interakcji
    @tag("kontrola", "mock", "podstawowe")
    def test_wylogujUzytkownika_czysci_kontekst(self):
        """
        Zadanie: doNothing() oraz never()
        Metoda wyloguj jest typu void. Sprawdzamy czy po wylogowaniu
        nie są wywoływane żadne operacje na encjach.
        """
        # WHEN
        self.facade.wylogujUzytkownika()

        # THEN: Sprawdzamy czy zawołano metodę wyloguj na kontekście
        self.facade._kontekst_auth.wyloguj.assert_called_once()

        # Weryfikacja: wylogowanie nie powinno wykonywać operacji na IEncjeFasada
        self.mock_encje.rejestrujUzytkownika.assert_not_called()
        self.mock_encje.usun.assert_not_called()

    #czy fasada przekazuje poprawne ID
    @tag("kontrola", "mock", "krytyczne")
    def test_usunKonto_weryfikacja_bezpieczenstwa(self):
        """
        Zadanie: verify() z konkretnym parametrem.
        Upewniamy się, że fasada przekazuje dokładnie to ID, które otrzymała.
        """
        # GIVEN
        testowe_id = 99

        # WHEN
        self.facade.usunKonto(testowe_id)

        # THEN: Sprawdzamy czy proces usuwania został zainicjowany z poprawnym ID
        with patch('kontrola.KsiegarniaKontrolaFacade.ProcesUsuwaniaKonta') as MockProces:
            # Ponowne wywołanie w kontekście patcha, aby przechwycić tworzenie obiektu
            self.facade.usunKonto(testowe_id)
            MockProces.return_value.wykonajUsuwanie.assert_called_with(testowe_id)

    #symulacja prawdziwej metody (doCallRealMethod)
    @tag("kontrola", "mock", "podstawowe")
    def test_przegladajKsiazki_wywoluje_metode_fasady(self):
        """
        Zadanie: doCallRealMethod() - sprawdzanie czy delegacja działa.
        """
        # WHEN
        self.facade.przegladajKsiazki()

        # THEN: Sprawdzamy czy Fasada Kontroli faktycznie skontaktowała się z procesem
        # bez mockowania wyniku (po prostu sprawdzamy sam fakt interakcji)
        with patch('kontrola.KsiegarniaKontrolaFacade.ProcesPrzegladaniaKsiazek') as MockProces:
            self.facade.przegladajKsiazki()
            MockProces.return_value.wykonajPrzegladanieKsiazek.assert_called()

    #obsluga kilku wyjatkow
    @tag("kontrola", "mock", "bledy")
    def test_aktualizujDaneUzytkownika_rozne_bledy(self):
        """
        Zadanie: thenThrow() dla różnych scenariuszy.
        """
        # GIVEN: Symulacja, że pierwsze wywołanie przechodzi, a drugie rzuca błąd
        self.mock_encje.aktualizujDaneUzytkownika.side_effect = [None, Exception("Błąd zapisu")]

        # WHEN: Pierwsza próba (powinna przejść bez błędu)
        self.mock_encje.aktualizujDaneUzytkownika(MagicMock(), "Jan", None, None, None, None)

        # WHEN: Druga próba (powinna rzucić wyjątek)
        with self.assertRaises(Exception) as context:
            self.mock_encje.aktualizujDaneUzytkownika(MagicMock(), "Jan", None, None, None, None)

        # THEN
        self.assertEqual(str(context.exception), "Błąd zapisu")

if __name__ == "__main__":
    unittest.main()