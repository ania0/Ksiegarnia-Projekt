
import unittest
from datetime import date
from typing import Optional
from encje.Zamowienie import Zamowienie
from encje.PozycjaZamowienia import PozycjaZamowienia
from encje.KsiazkaPapierowa import KsiazkaPapierowa
from encje.Uzytkownik import Uzytkownik  #  jako klienta

def tag(*tags):
    def decorator(func):
        func.tags = set(tags)
        return func
    return decorator

class TestZamowienie(unittest.TestCase):

    def setUp(self):
        # GIVEN – przygotowanie danych niezależnych
        self.ksiazka1 = KsiazkaPapierowa("Test1", "Autor1", 1234567891234, "SF", 20.0, 5, "Opis1")
        self.ksiazka2 = KsiazkaPapierowa("Test2", "Autor2", 1234567891224, "IT", 30.0, 3, "Opis2")
        self.pozycja1 = PozycjaZamowienia(self.ksiazka1, 2, 20.0)
        self.pozycja2 = PozycjaZamowienia(self.ksiazka2, 1, 30.0)
        self.klient = Uzytkownik("Jan", "Kowalski", "jan@example.com")
        self.zamowienie = Zamowienie()
        self.zamowienie._klient = self.klient

    def tearDown(self):
        # THEN – sprzątanie po teście
        self.zamowienie = None
        self.pozycja1 = None
        self.pozycja2 = None
        self.ksiazka1 = None
        self.ksiazka2 = None
        self.klient = None

    # TESTY NIEZALEŻNE
    @tag("encje", "zamowienie", "podstawowe")
    def test_pobierz_klienta_id(self):
        # GIVEN – istniejące zamówienie z przypisanym klientem
        # WHEN – pobieramy klienta i ID zamówienia
        klient = self.zamowienie.pobierzKlienta()
        id_zam = self.zamowienie.pobierzId()
        # THEN – klient nie jest None, to ten sam obiekt co self.klient, ID zamówienia None
        self.assertIsNotNone(klient)
        self.assertIs(klient, self.klient)
        self.assertIsNone(id_zam)
        self.assertIsInstance(klient, Uzytkownik)

    # TESTY ZALEŻNE
    @tag("encje", "zamowienie", "podstawowe")
    def test_oblicz_cene_pojedyncza_pozycja(self):
        # GIVEN – dodanie jednej pozycji do zamówienia
        self.zamowienie.dodajPozycje(self.pozycja1)
        # WHEN – obliczana jest cena całkowita zamówienia
        cena = self.zamowienie.obliczCene()
        # THEN – cena poprawna i większa niż 0
        self.assertEqual(cena, 40.0)  # 2 * 20
        self.assertGreater(cena, 0)

    @tag("encje", "zamowienie", "zaawansowane", "krytyczne")
    def test_oblicz_cene_wiele_pozycji(self):
        # GIVEN – dodanie kilku pozycji do zamówienia
        self.zamowienie.dodajPozycje(self.pozycja1)
        self.zamowienie.dodajPozycje(self.pozycja2)
        # WHEN – obliczana jest cena całkowita
        cena = self.zamowienie.obliczCene()
        # THEN – cena zgodna z sumą i typu float
        self.assertEqual(cena, 70.0)
        self.assertIsInstance(cena, float)

    @tag("encje", "zamowienie", "parametryzowane")
    def test_oblicz_cene_parametryzowane(self):
        # GIVEN – różne scenariusze ilości i ceny jednostkowej
        przypadki = [(1, 20.0), (2, 40.0), (5, 100.0)] # 1 * 20; 2 * 20; 5 * 20;
        for ilosc, oczekiwana in przypadki:
            with self.subTest(ilosc=ilosc):
                # WHEN – tworzymy pozycję i dodajemy do zamówienia
                pozycja = PozycjaZamowienia(self.ksiazka1, ilosc, 20.0)
                zam = Zamowienie()
                zam.dodajPozycje(pozycja)
                cena = zam.obliczCene()
                # THEN – cena zgodna z oczekiwaną i nieujemna
                self.assertEqual(cena, oczekiwana)
                self.assertGreaterEqual(cena, 0)

    @tag("encje", "zamowienie", "krytyczne")
    def test_dodaj_wiele_pozycji(self):
        # GIVEN – lista pozycji do dodania
        pozycje = [
            PozycjaZamowienia(self.ksiazka1, 1, 20.0),
            PozycjaZamowienia(self.ksiazka2, 2, 30.0)
        ]
        # WHEN – dodawane są pozycje do zamówienia
        for p in pozycje:
            self.zamowienie.dodajPozycje(p)
        cena = self.zamowienie.obliczCene()
        # THEN – cena i lista pozycji są zgodne
        self.assertEqual(cena, 80.0)
        self.assertIsNotNone(self.zamowienie._pozycjeZamowienia)
        self.assertEqual(len(self.zamowienie._pozycjeZamowienia), 2)

    # TESTY WALIDACYJNE
    @tag("encje", "zamowienie", "walidacja")
    def test_oblicz_cene_brak_pozycji(self):
        # GIVEN – brak pozycji w zamówieniu
        # WHEN / THEN – cena całkowita wynosi 0
        self.assertEqual(self.zamowienie.obliczCene(), 0.0)

    @tag("encje", "zamowienie", "walidacja")
    def test_brak_klienta(self):
        # GIVEN – zamówienie bez klienta
        zam = Zamowienie()
        zam._klient = None
        # WHEN / THEN – pobranie klienta zwraca None
        self.assertIsNone(zam.pobierzKlienta())

    @tag("encje", "zamowienie", "walidacja")
    def test_cena_jednostkowa_zero(self):
        # GIVEN – pozycja z ceną jednostkową zero
        zero_cena = PozycjaZamowienia(self.ksiazka1, 3, 0.0)
        # WHEN – dodajemy do zamówienia
        self.zamowienie.dodajPozycje(zero_cena)
        # THEN – cena całkowita 0
        self.assertEqual(self.zamowienie.obliczCene(), 0.0)

    @tag("encje", "zamowienie", "walidacja")
    def test_wiele_pozycji_sumarycznie(self):
        # GIVEN – dodanie dwóch różnych pozycji
        ksiazka2 = KsiazkaPapierowa("Test2", "Autor2", 1234567812567, "Gatunek2", 30.0, 2, "Opis2")
        pozycja2 = PozycjaZamowienia(ksiazka2, 2, 30.0)
        self.zamowienie.dodajPozycje(self.pozycja1) # 2 * 20
        self.zamowienie.dodajPozycje(pozycja2) # 2 * 30
        # WHEN / THEN – suma cen zgodna z oczekiwaniem
        self.assertEqual(self.zamowienie.obliczCene(), 40.0 + 60.0)

    # Brak setterów dla _id, _data, _status – publiczne operacje i zachowanie obiektu

    def test_id_domyslnie_none(self):
        # GIVEN – nowo utworzone zamówienie
        zam = Zamowienie()

        # WHEN – pobieramy ID
        id_zam = zam.pobierzId()

        # THEN – ID nie jest ustawione
        self.assertIsNone(id_zam)

    # @tag("encje", "zamowienie", "walidacja")
    # def test_ujemna_ilosc_pozycji(self):
    #     # GIVEN – pozycja z ujemną ilością
    #     ujemna = PozycjaZamowienia(self.ksiazka1, -1, 20.0)
    #     # WHEN – dodajemy do zamówienia
    #     self.zamowienie.dodajPozycje(ujemna)
    #     # THEN – cena sumaryczna jest ujemna
    #     self.assertEqual(self.zamowienie.obliczCene(), -20.0)

    # @tag("encje", "zamowienie", "walidacja")
    # def test_id_zamowienia(self):
    #     # GIVEN – nowy obiekt zamówienia
    #     # THEN – ID początkowo None, po przypisaniu poprawne
    #     self.assertIsNone(self.zamowienie.pobierzId())
    #     self.zamowienie._id = 100
    #     self.assertEqual(self.zamowienie.pobierzId(), 100)

    # @tag("encje", "zamowienie", "walidacja")
    # def test_ustaw_data(self):
    #     # GIVEN – data dzisiejsza
    #     dzis = date.today()
    #     # WHEN – przypisujemy do zamówienia
    #     self.zamowienie._data = dzis
    #     # THEN – data poprawnie ustawiona i typu date
    #     self.assertEqual(self.zamowienie._data, dzis)
    #     self.assertIsInstance(self.zamowienie._data, date)

    # @tag("encje", "zamowienie", "walidacja")
    # def test_status_i_metoda_platnosci(self):
    #     # GIVEN – status i metoda płatności
    #     self.zamowienie._status = "w realizacji"
    #     self.zamowienie._metodaPlatnosci = "karta"
    #     # THEN – wartości poprawnie przypisane
    #     self.assertEqual(self.zamowienie._status, "w realizacji")
    #     self.assertEqual(self.zamowienie._metodaPlatnosci, "karta")

if __name__ == "__main__":
    unittest.main()