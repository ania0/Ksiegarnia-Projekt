
# class Ebook(IKsiazka):
#     def __init__(self, tytul: str, autor: str, ISBN: int, gatunek: str,
#                  cena: float, sciezkaDoPliku: str, opis: str):
#         super().__init__(tytul, autor, ISBN, gatunek, cena, opis)
#         self.sciezkaDoPliku: str = sciezkaDoPliku
#
#     # Ponieważ dziedziczymy, implementacja jest identyczna jak w papierowej dla pól wspólnych,
#     # ale musi być obecna, bo metody w IKsiazka są abstrakcyjne.
#
#     def ustawTytul(self, tytul: str) -> None:
#         self.tytul = tytul
#
#     def ustawAutora(self, autor: str) -> None:
#         self.autor = autor
#
#     def ustawGatunek(self, gatunek: str) -> None:
#         self.gatunek = gatunek
#
#     def ustawCene(self, cena: float) -> None:
#         self.cena = cena
#
#     def ustawOpis(self, opis: str) -> None:
#         self.opis = opis
#
#     def pobierzCene(self) -> float:
#        return self.cena
#
#     def pobierzISBN(self) -> int:
#        return self.ISBN

import unittest
from encje.Ebook import Ebook

# operacje niezależne – poziom 1
# niezalezne operacje encji
# w odpowiedniej kolejności,
# różne asercje i parametryzacje


class TestEbook(unittest.TestCase):

    def setUp(self):
        # GIVEN – przygotowanie danych
        # przed każdym testem
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
        # THEN – sprzątanie po każdym teście
        self.ebook = None




    def test_sciezka_do_pliku_nie_jest_pusta(self):
        # WHEN - wykonujemy operację, którą testujemy
        sciezka = self.ebook.sciezkaDoPliku

        # THEN -  sprawdzamy wynik
        self.assertIsNotNone(sciezka)  # sprawdzamy, że ścieżka istnieje (nie jest None)
        self.assertTrue(sciezka.endswith(".pdf"))

    def test_pobierz_isbn_parametryzowany(self):
        # Test parametryzowany – sprawdzamy kilka wartości ISBN
        # GIVEN - przygotowanie danych
        dane = [999, 123456, 1] # do testu

        for isbn in dane:
            # pozwala wykonać kilka podtestów w jednej metodzie
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

                # WHEN – wykonujemy metodę, którą testujemy
                wynik = ebook.pobierzISBN()

                # THEN – sprawdzamy wynik
                self.assertEqual(wynik, isbn)

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


    def test_ustaw_tytul_autora_gatunek_opis(self):
        # WHEN – ustawiamy tytuł, autora, gatunek, opis
        self.ebook.ustawTytul("Nowy tytul")
        self.ebook.ustawAutora("Nowy autor")
        self.ebook.ustawGatunek("Nowy gatunek")
        self.ebook.ustawOpis("Nowy opis")
        # THEN – sprawdzamy wszystkie zmiany
        self.assertEqual(self.ebook.tytul, "Nowy tytul")
        self.assertEqual(self.ebook.autor, "Nowy autor")
        self.assertEqual(self.ebook.gatunek, "Nowy gatunek")
        self.assertEqual(self.ebook.opis, "Nowy opis")
        self.assertIsNotNone(self.ebook.tytul)
        self.assertIsNotNone(self.ebook.autor)

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
                # THEN – sprawdzamy poprawność ścieżki
                self.assertTrue(ebook.sciezkaDoPliku.endswith(sciezka.split('.')[-1]))
                self.assertIsNotNone(ebook.sciezkaDoPliku)

if __name__ == "__main__":
    unittest.main()


