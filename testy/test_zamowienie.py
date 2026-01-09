#
# class Zamowienie(ICena):
#     """
#     Klasa domenowa Zamowienie – na tym etapie zawiera tylko strukturę,
#     deklarację atrybutów i sygnatury operacji bez implementacji.
#     """
#
#     def __init__(self):
#         # Atrybuty podstawowe
#         self._data: Optional[date] = None
#         self._cenaRazem: Optional[float] = None
#         self._status: Optional[str] = None
#         self._metodaPlatnosci: Optional[str] = None
#         self._id: Optional[int] = None
#
#         # Asocjacja 1..1 z Klientem
#         self._klient: Klient = None
#
#         # Kompozycja: * PozycjaZamowienia
#         self._pozycjeZamowienia: List[PozycjaZamowienia] = []
#         # @AssociationMultiplicity *
#         # @AssociationKind Composition
#
#
#     def dodajPozycje(self, pozycja: PozycjaZamowienia) -> None:
#         """Dodaje pozycję do zamówienia i przelicza cenę."""
#         self._pozycjeZamowienia.append(pozycja)
#
#     def obliczCene(self) -> float:
#         """Oblicza sumaryczną cenę zamówienia na podstawie pozycji."""
#         return sum(p.ilosc * p.cenaJednostkowa for p in self._pozycjeZamowienia)
#
#     def pobierzId(self) -> int:
#         """Zwraca ID zamówienia."""
#         return self._id
#
#     def pobierzKlienta(self) -> Optional[Klient]:
#         """Zwraca klienta powiązanego z zamówieniem."""
#         return self._klient

import unittest
from datetime import date
from typing import Optional
from encje.Zamowienie import Zamowienie
from encje.PozycjaZamowienia import PozycjaZamowienia
from encje.KsiazkaPapierowa import KsiazkaPapierowa
from encje.Uzytkownik import Uzytkownik  # użyjemy jako klienta

def tag(*tags):
    def decorator(func):
        func.tags = set(tags)
        return func
    return decorator

class TestZamowienie(unittest.TestCase):

    def setUp(self):
        # GIVEN – przygotowanie danych niezależnych
        self.ksiazka1 = KsiazkaPapierowa("Test1", "Autor1", 1, "SF", 20.0, 5, "Opis1")
        self.ksiazka2 = KsiazkaPapierowa("Test2", "Autor2", 2, "IT", 30.0, 3, "Opis2")
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
        # WHEN – pobieramy klienta i id zamówienia
        klient = self.zamowienie.pobierzKlienta()
        id_zam = self.zamowienie.pobierzId()
        # THEN – sprawdzamy poprawność
        self.assertIsNotNone(klient)
        self.assertIs(klient, self.klient)
        self.assertIsNone(id_zam)  # na tym etapie id nie jest ustawione, wiec None
        self.assertIsInstance(klient, Uzytkownik) # klient jest instancją klasy Uzytkownik

    # TESTY ZALEŻNE
    @tag("encje", "zamowienie", "podstawowe")
    def test_oblicz_cene_pojedyncza_pozycja(self):
        # GIVEN – dodanie jednej pozycji do zamówienia
        self.zamowienie.dodajPozycje(self.pozycja1)

        # WHEN – obliczamy cenę
        cena = self.zamowienie.obliczCene()

        # THEN – sprawdzamy wynik
        self.assertEqual(cena, 40.0)  # 2 * 20
        self.assertGreater(cena, 0)  # cena powinna być większa niż 0

    @tag("encje", "zamowienie", "zaawansowane", "krytyczne")
    def test_oblicz_cene_wiele_pozycji(self):
        # GIVEN – dodanie wielu pozycji
        self.zamowienie.dodajPozycje(self.pozycja1)
        self.zamowienie.dodajPozycje(self.pozycja2)

        # WHEN
        cena = self.zamowienie.obliczCene()

        # THEN - sprawdzamy sumę cen
        self.assertEqual(cena, 70.0)  # 40 + 30
        self.assertIsInstance(cena, float)

    @tag("encje", "zamowienie", "parametryzowane")
    def test_oblicz_cene_parametryzowane(self):
        # Parametryzacja – różne ilości i ceny
        przypadki = [
            (1, 20.0),  # 1 sztuka po 20
            (2, 40.0),  # 2 sztuki po 20
            (5, 100.0)  # 5 sztuk po 20
        ]
        for ilosc, oczekiwana in przypadki:
            with self.subTest(ilosc=ilosc):
                # GIVEN
                pozycja = PozycjaZamowienia(self.ksiazka1, ilosc, 20.0)
                zam = Zamowienie()
                zam.dodajPozycje(pozycja)

                # WHEN
                cena = zam.obliczCene()

                # THEN
                self.assertEqual(cena, oczekiwana)
                self.assertGreaterEqual(cena, 0)

    # def test_oblicz_cene_brak_pozycji(self):
    #     # GIVEN – brak pozycji w zamówieniu
    #
    #     # WHEN
    #     cena = self.zamowienie.obliczCene()
    #
    #     # THEN - cena powinna być 0
    #     self.assertEqual(cena, 0.0)
    #     self.assertIsInstance(cena, float)

    @tag("encje", "zamowienie", "krytyczne")
    def test_dodaj_wiele_pozycji(self):
        # GIVEN – tworzymy kilka pozycji
        pozycje = [
            PozycjaZamowienia(self.ksiazka1, 1, 20.0),
            PozycjaZamowienia(self.ksiazka2, 2, 30.0)
        ]
        for p in pozycje:
            self.zamowienie.dodajPozycje(p)

        # WHEN
        cena = self.zamowienie.obliczCene()

        # THEN - sprawdzamy sumę i poprawność listy pozycji
        self.assertEqual(cena, 80.0)  # 1*20 + 2*30
        self.assertIsNotNone(self.zamowienie._pozycjeZamowienia)
        self.assertEqual(len(self.zamowienie._pozycjeZamowienia), 2)


if __name__ == "__main__":
    unittest.main()
