import unittest
from encje.KsiazkaPapierowa import KsiazkaPapierowa

def tag(*tags):
    def decorator(func):
        func.tags = set(tags)
        return func
    return decorator

class TestKsiazkaPapierowa(unittest.TestCase):

    def setUp(self):
        # GIVEN – przygotowanie danych
        self.ksiazka = KsiazkaPapierowa(
            tytul="Test",
            autor="Autor",
            ISBN=1234567890123,  # 13 cyfr
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
        self.assertEqual(cena, 50.0)
        self.assertIsNotNone(cena)
        self.assertTrue(cena >= 0)

    @tag("encje", "papierowa", "parametryzowane", "krytyczne")
    def test_ustaw_cene_parametryzowany(self):
        ceny = [10.0, 0.0, 100.5]
        for nowa_cena in ceny:
            with self.subTest(cena=nowa_cena):
                self.ksiazka.ustawCene(nowa_cena)
                self.assertEqual(self.ksiazka.pobierzCene(), nowa_cena)
                self.assertIsNotNone(self.ksiazka.pobierzCene())
                self.assertTrue(self.ksiazka.pobierzCene() >= 0)

    @tag("encje", "papierowa", "podstawowe")
    def test_ustaw_tytul_autora_gatunek_opis(self):
        self.ksiazka.ustawTytul("Nowy Tytul")
        self.ksiazka.ustawAutora("Nowy Autor")
        self.ksiazka.ustawGatunek("Nowy Gatunek")
        self.ksiazka.ustawOpis("Nowy Opis")

        self.assertEqual(self.ksiazka.tytul, "Nowy Tytul")
        self.assertEqual(self.ksiazka.autor, "Nowy Autor")
        self.assertEqual(self.ksiazka.gatunek, "Nowy Gatunek")
        self.assertEqual(self.ksiazka.opis, "Nowy Opis")
        self.assertIsNotNone(self.ksiazka.tytul)
        self.assertIsNotNone(self.ksiazka.autor)

    @tag("encje", "papierowa", "parametryzowane", "podstawowe")
    def test_stan_magazynowy_parametryzowany(self):
        stany = [0, 5, 100]
        for stan in stany:
            with self.subTest(stan=stan):
                ks = KsiazkaPapierowa(
                    tytul="Test",
                    autor="Autor",
                    ISBN=1234567890123,
                    gatunek="SF",
                    cena=50.0,
                    stanMagazynowy=stan,
                    opis="Opis"
                )
                self.assertEqual(ks.stanMagazynowy, stan)
                self.assertTrue(ks.stanMagazynowy >= 0)

    # Walidacje

    @tag("encje", "walidacja", "papierowa", "ISBN", "krytyczne")
    def test_invalid_ISBN_za_krotki(self):
        with self.assertRaises(ValueError) as context:
            KsiazkaPapierowa(
                tytul="Test",
                autor="Autor",
                ISBN=123,  # za krótki
                gatunek="SF",
                cena=50.0,
                stanMagazynowy=10,
                opis="Opis"
            )
        self.assertIn("ISBN musi mieć dokładnie 13 cyfr", str(context.exception))

    @tag("encje", "walidacja", "papierowa", "ISBN", "krytyczne")
    def test_invalid_ISBN_nie_liczba(self):
        with self.assertRaises(ValueError) as context:
            KsiazkaPapierowa(
                tytul="Test",
                autor="Autor",
                ISBN="123ABC7890123",  # nie liczba
                gatunek="SF",
                cena=50.0,
                stanMagazynowy=10,
                opis="Opis"
            )
        self.assertIn("ISBN musi mieć dokładnie 13 cyfr", str(context.exception))

    @tag("encje", "papierowa", "tytul", "krytyczne")
    def test_invalid_tytul_mala_litera(self):
        with self.assertRaises(ValueError) as context:
            KsiazkaPapierowa(
                tytul="niepoprawnyTytul",
                autor="Autor",
                ISBN=1234567890123,
                gatunek="SF",
                cena=50.0,
                stanMagazynowy=10,
                opis="Opis"
            )
        self.assertIn("Tytuł musi zaczynać się z wielkiej litery", str(context.exception))

    @tag("encje", "papierowa", "autor", "krytyczne")
    def test_invalid_autor_mala_litera(self):
        with self.assertRaises(ValueError) as context:
            KsiazkaPapierowa(
                tytul="PoprawnyTytul",
                autor="jan Kowalski",
                ISBN=1234567890123,
                gatunek="SF",
                cena=50.0,
                stanMagazynowy=10,
                opis="Opis"
            )
        self.assertIn("Każdy człon nazwy autora musi zaczynać się wielką literą", str(context.exception))

    @tag("encje", "papierowa", "gatunek", "krytyczne")
    def test_invalid_gatunek_pusty(self):
        with self.assertRaises(ValueError) as context:
            KsiazkaPapierowa(
                tytul="Test",
                autor="Autor",
                ISBN=1234567890123,
                gatunek="",
                cena=50.0,
                stanMagazynowy=10,
                opis="Opis"
            )
        self.assertIn("Pole 'gatunek' nie może być puste!", str(context.exception))

    @tag("encje", "papierowa", "opis", "krytyczne")
    def test_invalid_opis_pusty(self):
        with self.assertRaises(ValueError) as context:
            KsiazkaPapierowa(
                tytul="Test",
                autor="Autor",
                ISBN=1234567890123,
                gatunek="SF",
                cena=50.0,
                stanMagazynowy=10,
                opis=""
            )
        self.assertIn("Pole 'opis' nie może być puste!", str(context.exception))

    @tag("encje", "papierowa", "cena", "krytyczne") # czy trzeba dodac walidaje w klasie ksiazka papierowa ? nie działa
    def test_invalid_cena_ujemna(self):
        with self.assertRaises(ValueError):
            self.ksiazka.ustawCene(-10.0)

    @tag("encje", "papierowa", "cena", "krytyczne") # nie działa
    def test_invalid_cena_nie_liczba(self):
        with self.assertRaises(TypeError):
            self.ksiazka.ustawCene("dziesiec")


if __name__ == "__main__":
    unittest.main()
