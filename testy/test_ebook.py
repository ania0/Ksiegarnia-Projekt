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
            ISBN=999,
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
        dane = [999, 123456, 1] # do testu

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

    # def test_ustaw_cene_bledna(self):
    #     # WHEN / THEN – ustawienie ujemnej ceny powinno zgłosić wyjątek
    #     with self.assertRaises(ValueError):
    #         self.ebook.ustawCene(-10.0)

    @tag("encje", "ebook", "podstawowe")
    def test_ustaw_tytul_autora_gatunek_opis(self):
        # WHEN – ustawienie tytuł, autora, gatunek, opis
        self.ebook.ustawTytul("Nowy tytul")
        self.ebook.ustawAutora("Nowy autor")
        self.ebook.ustawGatunek("Nowy gatunek")
        self.ebook.ustawOpis("Nowy opis")
        # THEN – sprawdzenie zmian
        self.assertEqual(self.ebook.tytul, "Nowy tytul")
        self.assertEqual(self.ebook.autor, "Nowy autor")
        self.assertEqual(self.ebook.gatunek, "Nowy gatunek")
        self.assertEqual(self.ebook.opis, "Nowy opis")
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
                    ISBN=123,
                    gatunek="IT",
                    cena=20.0,
                    sciezkaDoPliku=sciezka,
                    opis="Opis"
                )
                # THEN – poprawność ścieżki
                self.assertTrue(ebook.sciezkaDoPliku.endswith(sciezka.split('.')[-1]))
                self.assertIsNotNone(ebook.sciezkaDoPliku)

if __name__ == "__main__":
    unittest.main()


