
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
        # GIVEN – istniejący użytkownik
        # WHEN – pobierane są pola id i email
        # THEN – wartości są zgodne i mają odpowiedni typ
        self.assertEqual(self.uzytkownik.pobierzId(), 1)
        self.assertEqual(self.uzytkownik.pobierzEmail(), "jan.kowalski@example.com")
        self.assertIsInstance(self.uzytkownik.pobierzId(), int)
        self.assertIsInstance(self.uzytkownik.pobierzEmail(), str)

    # SETTERY PARAMETRYZOWANE
    @tag("encje", "uzytkownik", "parametryzowane", "podstawowe")
    def test_settery_parametryzowane(self):
        # GIVEN – lista imion i nazwisk
        imiona = ["Adam", "Ewa", "Marek"]
        nazwiska = ["Nowak", "Kowalczyk", "Wiśniewski"]
        for imie, nazwisko in zip(imiona, nazwiska):
            with self.subTest(imie=imie, nazwisko=nazwisko):
                # WHEN – ustawiane są imię i nazwisko
                self.uzytkownik.ustawImie(imie)
                self.uzytkownik.ustawNazwisko(nazwisko)
                # THEN – pola zostały poprawnie przypisane
                self.assertEqual(self.uzytkownik.imie, imie)
                self.assertEqual(self.uzytkownik.nazwisko, nazwisko)

    @tag("encje", "uzytkownik", "parametryzowane", "podstawowe")
    def test_parametryzacja_email(self):
        # GIVEN – lista poprawnych emaili
        maile = ["a@b.com", "x@y.pl", "test@test.com"]
        for mail in maile:
            with self.subTest(mail=mail):
                # WHEN – ustawiany jest email
                self.uzytkownik.ustawEmail(mail)
                # THEN – email przypisany i zawiera '@'
                self.assertEqual(self.uzytkownik.email, mail)
                self.assertTrue("@" in self.uzytkownik.email)

    # TESTY ZALEŻNE
    @tag("encje", "uzytkownik", "krytyczne")
    def test_set_email_haslo_adres(self):
        # GIVEN – istniejący użytkownik
        # WHEN – ustawiany jest email, hasło i adres
        self.uzytkownik.ustawEmail("nowy.email@example.com")
        self.uzytkownik.ustawHaslo("noweHaslo456")
        self.uzytkownik.ustawAdres("ul. Testowa 2")
        # THEN – pola poprawnie ustawione
        self.assertEqual(self.uzytkownik.email, "nowy.email@example.com")
        self.assertEqual(self.uzytkownik.hashHasla, "noweHaslo456")
        self.assertEqual(self.uzytkownik.adres, "ul. Testowa 2")

    @tag("encje", "uzytkownik", "krytyczne")
    def test_weryfikuj_haslo(self):
        # GIVEN – istniejące hasło użytkownika
        # THEN – poprawne hasło zwraca True
        self.assertTrue(self.uzytkownik.weryfikujHaslo("tajne123"))
        # THEN – złe hasło zwraca False
        self.assertFalse(self.uzytkownik.weryfikujHaslo("zleHaslo"))
        # WHEN – ustawione zostaje puste hasło
        # THEN – ValueError
        with self.assertRaises(ValueError):
            self.uzytkownik.ustawHaslo("")

    @tag("encje", "uzytkownik", "parametryzowane", "krytyczne")
    def test_weryfikuj_haslo_parametryzowane(self):
        # GIVEN – scenariusze hasło/oczekiwany wynik
        scenariusze = [
            ("tajne123", True),
            ("zleHaslo", False),
        ]
        for haslo, oczekiwany in scenariusze:
            with self.subTest(haslo=haslo):
                # WHEN – ustawiane jest hasło i sprawdzana weryfikacja
                self.uzytkownik.ustawHaslo(haslo)
                wynik = self.uzytkownik.weryfikujHaslo("tajne123")
                # THEN – wynik zgodny z oczekiwanym
                self.assertEqual(wynik, oczekiwany)

        # WHEN – ustawienie pustego hasła
        # THEN – ValueError
        with self.assertRaises(ValueError):
            self.uzytkownik.ustawHaslo("")

    # @tag("encje", "uzytkownik", "opcjonalne")
    # def test_none_opcjonalne_pola(self):
    #     # GIVEN – nowy użytkownik bez opcjonalnych pól
    #     uzytk = Uzytkownik(imie="Anna", nazwisko="Nowak", email="anna@example.com")
    #     # THEN – pola opcjonalne są None
    #     self.assertIsNone(uzytk.id)
    #     self.assertIsNone(uzytk.adres)
    #     self.assertIsNone(uzytk.hashHasla)

    # WALIDACJE
    @tag("encje", "uzytkownik", "walidacja")
    def test_invalid_imie_nazwisko_email(self):
        # GIVEN – niepoprawne dane
        # THEN – ValueError
        with self.assertRaises(ValueError):
            Uzytkownik(imie="jan", nazwisko="Kowalski", email="a@b.com")
        with self.assertRaises(ValueError):
            Uzytkownik(imie="Jan", nazwisko="kowalski", email="a@b.com")
        with self.assertRaises(ValueError):
            Uzytkownik(imie="Jan", nazwisko="Kowalski", email="abc.com")
        with self.assertRaises(ValueError):
            Uzytkownik(imie="Jan", nazwisko="Kowalski", email="abc@com")


    @tag("encje", "uzytkownik", "walidacja")
    def test_settery_invalid(self):
        # GIVEN – istniejący użytkownik
        # THEN – ustawienie błędnych danych powoduje ValueError
        with self.assertRaises(ValueError):
            self.uzytkownik.ustawImie("jan")
        with self.assertRaises(ValueError):
            self.uzytkownik.ustawNazwisko("kowalski")
        with self.assertRaises(ValueError):
            self.uzytkownik.ustawEmail("abc.com")
        with self.assertRaises(ValueError):
            self.uzytkownik.ustawEmail("abc@com")
        with self.assertRaises(ValueError):
            self.uzytkownik.ustawHaslo("")

if __name__ == "__main__":
    unittest.main()