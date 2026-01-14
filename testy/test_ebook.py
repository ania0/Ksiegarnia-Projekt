import unittest
from encje.Ebook import Ebook

# niezalezne operacje encji - różne asercje i parametryzacje

def tag(*tags):
    def decorator(func):
        func.tags = set(tags)
        return func
    return decorator

class TestEbook(unittest.TestCase):

    def setUp(self):
        # GIVEN – przygotowanie danych przed kazdym testem
        self.ebook = Ebook(
            tytul="Ebook",
            autor="Autor",
            ISBN=1234567890123,  # 13 cyfr
            gatunek="IT",
            cena=30.0,
            sciezkaDoPliku="/tmp/book.pdf",
            opis="Opis"
        )

    def tearDown(self):
        # THEN – sprzatanie po kazdym tescie
        self.ebook = None

    @tag("encje", "ebook", "podstawowe")
    def test_sciezka_do_pliku_nie_jest_pusta(self):
        # WHEN - testowane operacje
        sciezka = self.ebook.sciezkaDoPliku

        # THEN -  sprawdzanie wyniku
        self.assertIsNotNone(sciezka)  # czy sciezka istnieje (nie None)
        self.assertTrue(sciezka.endswith(".pdf"))

    @tag("encje", "ebook", "parametryzowane", "krytyczne")
    def test_pobierz_isbn_parametryzowany(self):
        # Test parametryzowany – sprawdzenie kilka wartości ISBN
        # GIVEN - przygotowanie danych
        dane = [1234567891023, 1234567891234] # do testu

        for isbn in dane:
            # kilka podtestów w jednej metodzie
            with self.subTest(isbn=isbn):
                ebook = Ebook(
                    tytul="Test",
                    autor="Autor",
                    ISBN=isbn,
                    gatunek="IT",
                    cena=10.0,
                    sciezkaDoPliku="/tmp/a.pdf",
                    opis="Opis"
                )

                # WHEN –wykonanie testowanej metody
                wynik = ebook.pobierzISBN()

                # THEN – sprawdzenie wyniku
                self.assertEqual(wynik, isbn)

    @tag("encje", "ebook", "parametryzowane", "podstawowe")
    def test_ustaw_cene_parametryzowany(self):
        # Parametryzowany test ceny
        ceny = [10.0, 0.0, 100.5]
        for cena in ceny:
            with self.subTest(cena=cena):
                self.ebook.ustawCene(cena)
                self.assertEqual(self.ebook.pobierzCene(), cena)
                self.assertIsNotNone(self.ebook.pobierzCene())
                self.assertTrue(self.ebook.pobierzCene() >= 0)


    @tag("encje", "ebook", "podstawowe")
    def test_ustaw_tytul_autora_gatunek_opis(self):
        # WHEN – ustawienie tytuł, autora, gatunek, opis
        self.ebook.ustawTytul("Nowy Tytul")
        self.ebook.ustawAutora("Nowy Autor")
        self.ebook.ustawGatunek("Nowy Gatunek")
        self.ebook.ustawOpis("Nowy Opis")
        # THEN – sprawdzenie zmian
        self.assertEqual(self.ebook.tytul, "Nowy Tytul")
        self.assertEqual(self.ebook.autor, "Nowy Autor")
        self.assertEqual(self.ebook.gatunek, "Nowy Gatunek")
        self.assertEqual(self.ebook.opis, "Nowy Opis")
        self.assertIsNotNone(self.ebook.tytul)
        self.assertIsNotNone(self.ebook.autor)

    @tag("encje", "ebook", "parametryzowane", "podstawowe")
    def test_sciezka_do_pliku_parametryzowany(self):
        # GIVEN – różne ścieżki do pliku
        sciezki = ["/tmp/a.pdf", "/tmp/b.epub", "/tmp/c.mobi"]
        for sciezka in sciezki:
            with self.subTest(sciezka=sciezka):
                ebook = Ebook(
                    tytul="Test",
                    autor="Autor",
                    ISBN=1234567890123,  # 13 cyfr
                    gatunek="IT",
                    cena=20.0,
                    sciezkaDoPliku=sciezka,
                    opis="Opis"
                )
                # THEN – poprawność ścieżki
                self.assertTrue(ebook.sciezkaDoPliku.endswith(sciezka.split('.')[-1]))
                self.assertIsNotNone(ebook.sciezkaDoPliku)

    # Dodatkowe testy walidacyjne

    @tag("encje", "walidacja", "ebook", "ISBN", "krytyczne")
    def test_invalid_ISBN_za_krotki(self):
        # WHEN / THEN – ISBN krótszy niż 13 cyfr
        with self.assertRaises(ValueError) as context:
            Ebook(
                tytul="Test",
                autor="Autor",
                ISBN=123456789,  # za krótki
                gatunek="IT",
                cena=10.0,
                sciezkaDoPliku="/tmp/a.pdf",
                opis="Opis"
            )
        self.assertIn("ISBN musi mieć dokładnie 13 cyfr", str(context.exception))


    @tag("encje", "walidacja", "ebook", "ISBN", "krytyczne") # ?
    def test_invalid_isbn_nie_liczba(self):
        # GIVEN – ISBN zawiera znaki niebędące cyframi
        isbn = "123ABC7890123"

        # WHEN / THEN – próba utworzenia Ebook powinna podnieść ValueError
        with self.assertRaises(ValueError) as context:
            Ebook(
                tytul="Test",
                autor="Autor",
                ISBN=isbn,  # ISBN nie jest liczbą całkowitą
                gatunek="IT",
                cena=10.0,
                sciezkaDoPliku="/tmp/a.pdf",
                opis="Opis"
            )

        # THEN – sprawdzamy komunikat o błędzie aktualnie stosowany w klasie
        self.assertIn("ISBN musi mieć dokładnie 13 cyfr", str(context.exception))

    @tag("encje", "ebook", "tytul", "krytyczne")
    def test_invalid_tytul_mala_litera(self):
        # WHEN / THEN – tytuł zaczyna się małą literą
        with self.assertRaises(ValueError) as context:
            Ebook(
                tytul="niepoprawnyTytul", #tytul z malej litery
                autor="Autor",
                ISBN=1234567890123,
                gatunek="IT",
                cena=10.0,
                sciezkaDoPliku="/tmp/a.pdf",
                opis="Opis"
            )
        self.assertIn("Tytuł musi zaczynać się z wielkiej litery", str(context.exception))

    @tag("encje", "ebook", "autor", "krytyczne")
    def test_invalid_autor_mala_litera(self):
        # WHEN / THEN – imię/nazwisko autora z małą literą
        with self.assertRaises(ValueError) as context:
            Ebook(
                tytul="PoprawnyTytul",
                autor="jan Kowalski",  # imię z małej litery
                ISBN=1234567890123,
                gatunek="IT",
                cena=10.0,
                sciezkaDoPliku="/tmp/a.pdf",
                opis="Opis"
            )
        self.assertIn("Każdy człon nazwy autora musi zaczynać się wielką literą", str(context.exception))

    @tag("encje", "ebook", "autor", "krytyczne")
    def test_invalid_autor_zle_nazwisko(self):
        # WHEN / THEN – nazwisko z małej litery
        with self.assertRaises(ValueError):
            Ebook(
                tytul="PoprawnyTytul",
                autor="Jan kowalski",  # nazwisko z małej litery
                ISBN=1234567890123,
                gatunek="IT",
                cena=10.0,
                sciezkaDoPliku="/tmp/a.pdf",
                opis="Opis"
            )

    @tag("encje", "walidacja", "ebook", "gatunek", "krytyczne")
    def test_invalid_gatunek_pusty(self):
        with self.assertRaises(ValueError) as context:
            Ebook(
                tytul="Test",
                autor="Autor",
                ISBN=1234567890123,
                gatunek="",  # pusty gatunek
                cena=10.0,
                sciezkaDoPliku="/tmp/a.pdf",
                opis="Opis"
            )
        self.assertIn("Pole 'gatunek' nie może być puste", str(context.exception))

    @tag("encje", "walidacja", "ebook", "opis", "krytyczne")
    def test_invalid_opis_pusty(self):
        with self.assertRaises(ValueError) as context:
            Ebook(
                tytul="Test",
                autor="Autor",
                ISBN=1234567890123,
                gatunek="IT",
                cena=10.0,
                sciezkaDoPliku="/tmp/a.pdf",
                opis=""  # pusty opis
            )
        self.assertIn("Pole 'opis' nie może być puste", str(context.exception))

    @tag("encje", "walidacja", "ebook", "cena", "krytyczne")
    def test_invalid_cena_ujemna(self):
        with self.assertRaises(ValueError) as context:
            Ebook(
                tytul="Test",
                autor="Autor",
                ISBN=1234567890123,
                gatunek="IT",
                cena=-10.0,  # ujemna cena
                sciezkaDoPliku="/tmp/a.pdf",
                opis="Opis"
            )
        self.assertIn("Cena nie może być ujemna", str(context.exception))

    @tag("encje", "walidacja", "ebook", "cena", "krytyczne")
    def test_invalid_cena_nie_liczba(self):
        with self.assertRaises(ValueError) as context:
            Ebook(
                tytul="Test",
                autor="Autor",
                ISBN=1234567890123,
                gatunek="IT",
                cena="dziesiec",
                sciezkaDoPliku="/tmp/a.pdf",
                opis="Opis"
            )
        self.assertIn("Cena musi być liczbą", str(context.exception))

    @tag("encje", "walidacja", "ebook", "cena", "krytyczne")
    def test_cena_ujemna(self):
        with self.assertRaises(ValueError) as context:
            Ebook(
                tytul="Test",
                autor="Autor",
                ISBN=1234567890123,
                gatunek="IT",
                cena=-10,  # <-- ujemna cena jako float/int
                sciezkaDoPliku="/tmp/a.pdf",
                opis="Opis"
            )
        self.assertIn("Cena nie może być ujemna", str(context.exception))

    @tag("encje", "walidacja", "ebook", "cena", "krytyczne")
    def test_cena_nie_liczba(self):
        with self.assertRaises(ValueError) as context:
            Ebook(
                tytul="Test",
                autor="Autor",
                ISBN=1234567890123,
                gatunek="IT",
                cena="dziesiec",  # niepoprawna cena
                sciezkaDoPliku="/tmp/a.pdf",
                opis="Opis"
            )
        self.assertIn("Cena musi być liczbą", str(context.exception))


if __name__ == "__main__":
    unittest.main()


