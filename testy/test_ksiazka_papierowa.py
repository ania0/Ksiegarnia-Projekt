

def tag(*tags):
    def decorator(func):
        func.tags = set(tags)
        return func
    return decorator

import unittest
from encje.KsiazkaPapierowa import KsiazkaPapierowa

class TestKsiazkaPapierowa(unittest.TestCase):

    def setUp(self):
        # GIVEN – przygotowanie danych
        self.ksiazka = KsiazkaPapierowa(
            tytul="Test",
            autor="Autor",
            ISBN=123,
            gatunek="SF",
            cena=50.0,
            stanMagazynowy=10,
            opis="Opis"
        )

    def tearDown(self):
        # THEN – sprzątanie po teście
        self.ksiazka = None

    @tag("encje", "papierowa", "podstawowe")
    def test_pobierz_cene(self):
        # WHEN – pobranie ceny
        cena = self.ksiazka.pobierzCene()
        # THEN – sprawdzenie wyniku
        self.assertEqual(cena, 50.0)  # assertEqual

    @tag("encje", "papierowa", "parametryzowane", "krytyczne")
    def test_ustaw_cene_parametryzowany(self):
        # GIVEN – różne ceny do ustawienia
        ceny = [10.0, 0.0, 100.5]
        for nowa_cena in ceny:
            with self.subTest(cena=nowa_cena):
                # WHEN – ustawienie ceny
                self.ksiazka.ustawCene(nowa_cena)
                # THEN – sprawdzenie, czy cena została poprawnie ustawiona
                self.assertEqual(self.ksiazka.cena, nowa_cena)
                self.assertIsNotNone(self.ksiazka.cena)
                self.assertTrue(self.ksiazka.cena >= 0)

    # def test_ustaw_cene_bledna(self):
    #     # WHEN / THEN – ustawienie ujemnej ceny powinno zgłosić wyjątek
    #     with self.assertRaises(ValueError):
    #         self.ksiazka.ustawCene(-10.0)

    @tag("encje", "papierowa", "podstawowe")
    def test_ustaw_tytul_autora_gatunek_opis(self):
        # WHEN – zmiana tytułu, autora, gatunku i opisu
        self.ksiazka.ustawTytul("Nowy tytul")
        self.ksiazka.ustawAutora("Nowy autor")
        self.ksiazka.ustawGatunek("Nowy gatunek")
        self.ksiazka.ustawOpis("Nowy opis")
        # THEN – sprawdzenie poprawności zmian
        self.assertEqual(self.ksiazka.tytul, "Nowy tytul")
        self.assertEqual(self.ksiazka.autor, "Nowy autor")
        self.assertEqual(self.ksiazka.gatunek, "Nowy gatunek")
        self.assertEqual(self.ksiazka.opis, "Nowy opis")
        self.assertIsNotNone(self.ksiazka.tytul)
        self.assertIsNotNone(self.ksiazka.autor)

    @tag("encje", "papierowa", "parametryzowane", "podstawowe")
    def test_stan_magazynowy_parametryzowany(self):
        # GIVEN – różne wartości stanu magazynowego
        stany = [0, 5, 100]
        for stan in stany:
            with self.subTest(stan=stan):
                ks = KsiazkaPapierowa(
                    tytul="Test",
                    autor="Autor",
                    ISBN=123,
                    gatunek="SF",
                    cena=50.0,
                    stanMagazynowy=stan,
                    opis="Opis"
                )
                # THEN – sprawdzenie poprawności stanu magazynowego
                self.assertEqual(ks.stanMagazynowy, stan)
                if stan > 0:
                    self.assertTrue(ks.stanMagazynowy > 0)
                else:
                    self.assertFalse(ks.stanMagazynowy > 0)

    # def test_stan_magazynowy_bledny(self):
    #     # WHEN / THEN – ujemny stan magazynowy powinien zgłosić wyjątek
    #     with self.assertRaises(ValueError):
    #         KsiazkaPapierowa(
    #             tytul="Test",
    #             autor="Autor",
    #             ISBN=123,
    #             gatunek="SF",
    #             cena=50.0,
    #             stanMagazynowy=-5,
    #             opis="Opis"
    #         )

if __name__ == "__main__":
    unittest.main()
