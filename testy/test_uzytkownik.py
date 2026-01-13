
import unittest
from typing import Optional
from encje.Uzytkownik import Uzytkownik

def tag(*tags):
    def decorator(func):
        func.tags = set(tags)
        return func
    return decorator


class TestUzytkownik(unittest.TestCase):
    def setUp(self):
        # GIVEN – przygotowanie danych
        self.uzytkownik = Uzytkownik(
            imie="Jan",
            nazwisko="Kowalski",
            email="jan.kowalski@example.com",
            hashHasla="tajne123",
            adres="ul. Przykładowa 1",
            id=1
        )

    def tearDown(self):
        # THEN – sprzątanie po każdym teście
        self.uzytkownik = None

    # TESTY NIEZALEŻNE
    @tag("encje", "uzytkownik", "podstawowe")
    def test_gettery(self):
        # WHEN – pobiera dane użytkownika
        identyfikator = self.uzytkownik.pobierzId()
        email = self.uzytkownik.pobierzEmail()
        # THEN – sprawdza poprawność wartości
        self.assertEqual(identyfikator, 1)
        self.assertEqual(email, "jan.kowalski@example.com")
        self.assertIsNotNone(email)
        self.assertIsNotNone(identyfikator)
        self.assertIsInstance(identyfikator, int)
        self.assertIsInstance(email, str)

    @tag("encje", "uzytkownik", "podstawowe")
    def test_settery_parametryzowane(self):
        # Parametryzacja
        imiona = ["Adam", "Ewa", "Marek"]
        nazwiska = ["Nowak", "Kowalczyk", "Wiśniewski"]

        for imie, nazwisko in zip(imiona, nazwiska):
            with self.subTest(imie=imie, nazwisko=nazwisko):
                # WHEN – ustawia nowe dane
                self.uzytkownik.ustawImie(imie)
                self.uzytkownik.ustawNazwisko(nazwisko)
                # THEN – sprawdza czy zmiany zostały zastosowane
                self.assertEqual(self.uzytkownik.imie, imie)
                self.assertEqual(self.uzytkownik.nazwisko, nazwisko)
                self.assertIsNotNone(self.uzytkownik.imie)
                self.assertIsNotNone(self.uzytkownik.nazwisko)

    @tag("encje", "uzytkownik", "parametryzowane", "podstawowe")
    def test_parametryzacja_email(self):
        # GIVEN – różne maile do testu
        maile = ["a@b.com", "x@y.pl", "test@test.com"]
        for mail in maile:
            with self.subTest(mail=mail):
                # WHEN
                self.uzytkownik.ustawEmail(mail)
                # THEN
                self.assertEqual(self.uzytkownik.email, mail)
                self.assertIsNotNone(self.uzytkownik.email)
                self.assertTrue("@" in self.uzytkownik.email)

    # TESTY ZALEŻNE
    @tag("encje", "uzytkownik", "krytyczne")
    def test_set_email_haslo_adres(self):
        # WHEN – zmiana email, hasła i adresu
        self.uzytkownik.ustawEmail("nowy.email@example.com")
        self.uzytkownik.ustawHaslo("noweHaslo456")
        self.uzytkownik.ustawAdres("ul. Testowa 2")
        # THEN – sprawdza czy wartości zostały poprawnie zmienione
        self.assertEqual(self.uzytkownik.email, "nowy.email@example.com")
        self.assertEqual(self.uzytkownik.hashHasla, "noweHaslo456")
        self.assertEqual(self.uzytkownik.adres, "ul. Testowa 2")
        self.assertIsNotNone(self.uzytkownik.email)
        self.assertIsNotNone(self.uzytkownik.hashHasla)
        self.assertIsNotNone(self.uzytkownik.adres)

    @tag("encje", "uzytkownik", "krytyczne")
    def test_weryfikuj_haslo(self):
        # WHEN / THEN – poprawne hasło
        self.assertTrue(self.uzytkownik.weryfikujHaslo("tajne123"))
        # WHEN / THEN – niepoprawne hasło
        self.assertFalse(self.uzytkownik.weryfikujHaslo("zleHaslo"))
        # WHEN / THEN – brak hasła
        self.uzytkownik.ustawHaslo(None)
        self.assertFalse(self.uzytkownik.weryfikujHaslo("tajne123"))

    @tag("encje", "uzytkownik","parametryzowane", "krytyczne")
    def test_weryfikuj_haslo_parametryzowane(self):
        # GIVEN – różne scenariusze haseł
        hasla = [("tajne123", True), ("zleHaslo", False), (None, False)]
        for haslo, oczekiwany in hasla:
            with self.subTest(haslo=haslo):
                self.uzytkownik.ustawHaslo(haslo)
                wynik = self.uzytkownik.weryfikujHaslo("tajne123")
                # THEN
                self.assertEqual(wynik, oczekiwany)

    @tag("encje", "uzytkownik", "opcjonalne")
    def test_none_opcjonalne_pola(self):
        # GIVEN – tworzy użytkownika z brakującymi opcjonalnymi polami
        uzytk = Uzytkownik(imie="Anna", nazwisko="Nowak", email="anna@example.com")
        # THEN – pola opcjonalne powinny być None
        self.assertIsNone(uzytk.id)
        self.assertIsNone(uzytk.adres)
        self.assertIsNone(uzytk.hashHasla)

if __name__ == "__main__":
    unittest.main()
