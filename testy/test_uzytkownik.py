
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
    # GETTERY
    @tag("encje", "uzytkownik", "podstawowe")
    def test_gettery(self):
        self.assertEqual(self.uzytkownik.pobierzId(), 1)
        self.assertEqual(self.uzytkownik.pobierzEmail(), "jan.kowalski@example.com")
        self.assertIsInstance(self.uzytkownik.pobierzId(), int)
        self.assertIsInstance(self.uzytkownik.pobierzEmail(), str)

    # SETTERY PARAMETRYZOWANE
    @tag("encje", "uzytkownik", "parametryzowane", "podstawowe")
    def test_settery_parametryzowane(self):
        imiona = ["Adam", "Ewa", "Marek"]
        nazwiska = ["Nowak", "Kowalczyk", "Wiśniewski"]
        for imie, nazwisko in zip(imiona, nazwiska):
            with self.subTest(imie=imie, nazwisko=nazwisko):
                self.uzytkownik.ustawImie(imie)
                self.uzytkownik.ustawNazwisko(nazwisko)
                self.assertEqual(self.uzytkownik.imie, imie)
                self.assertEqual(self.uzytkownik.nazwisko, nazwisko)


    @tag("encje", "uzytkownik", "parametryzowane", "podstawowe")
    def test_parametryzacja_email(self):
        maile = ["a@b.com", "x@y.pl", "test@test.com"]
        for mail in maile:
            with self.subTest(mail=mail):
                self.uzytkownik.ustawEmail(mail)
                self.assertEqual(self.uzytkownik.email, mail)
                self.assertTrue("@" in self.uzytkownik.email)

    # TESTY ZALEŻNE
    @tag("encje", "uzytkownik", "krytyczne")
    def test_set_email_haslo_adres(self):
        self.uzytkownik.ustawEmail("nowy.email@example.com")
        self.uzytkownik.ustawHaslo("noweHaslo456")
        self.uzytkownik.ustawAdres("ul. Testowa 2")
        self.assertEqual(self.uzytkownik.email, "nowy.email@example.com")
        self.assertEqual(self.uzytkownik.hashHasla, "noweHaslo456")
        self.assertEqual(self.uzytkownik.adres, "ul. Testowa 2")

    @tag("encje", "uzytkownik", "krytyczne")
    def test_weryfikuj_haslo(self):
        self.assertTrue(self.uzytkownik.weryfikujHaslo("tajne123"))
        self.assertFalse(self.uzytkownik.weryfikujHaslo("zleHaslo"))
        # ustawienie pustego hasła powinno zgłosić wyjątek
        with self.assertRaises(ValueError):
            self.uzytkownik.ustawHaslo("")

    @tag("encje", "uzytkownik", "parametryzowane", "krytyczne")
    def test_weryfikuj_haslo_parametryzowane(self):
        scenariusze = [
            ("tajne123", True),  # poprawne hasło
            ("zleHaslo", False),  # niepoprawne hasło
        ]

        for haslo, oczekiwany in scenariusze:
            with self.subTest(haslo=haslo):
                self.uzytkownik.ustawHaslo(haslo)
                wynik = self.uzytkownik.weryfikujHaslo("tajne123")
                self.assertEqual(wynik, oczekiwany)

        # test ustawienia pustego hasła powinien zgłosić wyjątek
        with self.assertRaises(ValueError):
            self.uzytkownik.ustawHaslo("")

    @tag("encje", "uzytkownik", "opcjonalne")
    def test_none_opcjonalne_pola(self):
        uzytk = Uzytkownik(imie="Anna", nazwisko="Nowak", email="anna@example.com")
        self.assertIsNone(uzytk.id)
        self.assertIsNone(uzytk.adres)
        self.assertIsNone(uzytk.hashHasla)

    # WALIDACJE
    @tag("encje", "uzytkownik", "walidacja")
    def test_invalid_imie_nazwisko_email(self):
        # imię małą literą
        with self.assertRaises(ValueError):
            Uzytkownik(imie="jan", nazwisko="Kowalski", email="a@b.com")
        # nazwisko małą literą
        with self.assertRaises(ValueError):
            Uzytkownik(imie="Jan", nazwisko="kowalski", email="a@b.com")
        # brak @ w email
        with self.assertRaises(ValueError):
            Uzytkownik(imie="Jan", nazwisko="Kowalski", email="abc.com")
        # brak kropki po @
        with self.assertRaises(ValueError):
            Uzytkownik(imie="Jan", nazwisko="Kowalski", email="abc@com")

    @tag("encje", "uzytkownik", "walidacja")
    def test_settery_invalid(self):
        # błędne imię
        with self.assertRaises(ValueError):
            self.uzytkownik.ustawImie("jan")
        # błędne nazwisko
        with self.assertRaises(ValueError):
            self.uzytkownik.ustawNazwisko("kowalski")
        # błędny email
        with self.assertRaises(ValueError):
            self.uzytkownik.ustawEmail("abc.com")
        with self.assertRaises(ValueError):
            self.uzytkownik.ustawEmail("abc@com")
        # puste hasło
        with self.assertRaises(ValueError):
            self.uzytkownik.ustawHaslo("")

if __name__ == "__main__":
    unittest.main()
