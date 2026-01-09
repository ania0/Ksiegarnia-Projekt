import unittest
# Importowanie klas testowych z Twoich plików
from test_ebook import TestEbook
from test_ksiazka_papierowa import TestKsiazkaPapierowa
from test_uzytkownik import TestUzytkownik
from test_zamowienie import TestZamowienie
from testy_zad2 import TestKsiegarniaKontrolaMock


# --- POMOCNIK FILTROWANIA (Symulacja @IncludeTags / @ExcludeTags) ---
class SuiteHelper:
    @staticmethod
    def filtruj_testy(zestaw_wejsciowy, include=None, exclude=None):
        """Przeszukuje zestaw i wybiera testy na podstawie tagów."""
        nowy_zestaw = unittest.TestSuite()
        for test in zestaw_wejsciowy:
            # Jeśli element to pod-zestaw (TestSuite), przeszukaj go rekurencyjnie
            if isinstance(test, unittest.TestSuite):
                podzestaw = SuiteHelper.filtruj_testy(test, include, exclude)
                if podzestaw.countTestCases() > 0:
                    nowy_zestaw.addTest(podzestaw)
            else:
                # Pobierz metodę testową i jej tagi
                metoda = getattr(test, test._testMethodName)
                tagi_metody = getattr(metoda, 'tags', set())

                # Logika @IncludeTags: jeśli zdefiniowano, tag musi być w tagach metody
                if include and not (set(include) & tagi_metody):
                    continue
                # Logika @ExcludeTags: jeśli zdefiniowano, tag NIE może być w tagach metody
                if exclude and (set(exclude) & tagi_metody):
                    continue

                nowy_zestaw.addTest(test)
        return nowy_zestaw


# --- ZESTAWY TESTÓW (SUITES) ---

class SuiteEncje:
    """Odpowiednik @Suite + @SelectClasses (Warstwa Encji)"""

    @staticmethod
    def pobierz():
        suite = unittest.TestSuite()
        loader = unittest.TestLoader()
        # Wybieramy konkretne klasy warstwy encji
        suite.addTests(loader.loadTestsFromTestCase(TestEbook))
        suite.addTests(loader.loadTestsFromTestCase(TestKsiazkaPapierowa))
        suite.addTests(loader.loadTestsFromTestCase(TestUzytkownik))
        suite.addTests(loader.loadTestsFromTestCase(TestZamowienie))
        return suite


class SuiteKontrola:
    """Odpowiednik @Suite + @SelectPackages (Warstwa Kontroli)"""

    @staticmethod
    def pobierz():
        loader = unittest.TestLoader()
        # Wybieramy testy z warstwy kontroli (Mocki)
        return loader.loadTestsFromTestCase(TestKsiegarniaKontrolaMock)


class SuiteKrytyczne:
    """Odpowiednik @Suite + @IncludeTags('krytyczne')"""

    @staticmethod
    def pobierz():
        # Pobieramy wszystkie możliwe testy
        loader = unittest.TestLoader()
        wszystkie = unittest.TestSuite([
            loader.loadTestsFromTestCase(TestEbook),
            loader.loadTestsFromTestCase(TestKsiazkaPapierowa),
            loader.loadTestsFromTestCase(TestUzytkownik),
            loader.loadTestsFromTestCase(TestZamowienie),
            loader.loadTestsFromTestCase(TestKsiegarniaKontrolaMock)
        ])
        # Filtrujemy tylko te, które mają tag "krytyczne"
        return SuiteHelper.filtruj_testy(wszystkie, include=["krytyczne"])


class SuitePodstawowe:
    """Odpowiednik @Suite + @ExcludeTags('zaawansowane', 'bledy')"""

    @staticmethod
    def pobierz():
        loader = unittest.TestLoader()
        wszystkie = unittest.TestSuite([
            loader.loadTestsFromTestCase(TestUzytkownik),
            loader.loadTestsFromTestCase(TestZamowienie),
            loader.loadTestsFromTestCase(TestKsiegarniaKontrolaMock)
        ])
        # Wykluczamy testy trudne (zaawansowane) i testy wyjątków (bledy)
        return SuiteHelper.filtruj_testy(wszystkie, exclude=["zaawansowane", "bledy"])


# --- URUCHAMIANIE WSZYSTKIEGO ---

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)

    print("\n" + "=" * 50)
    print("URUCHAMIANIE ZESTAWU: WARSTWA ENCJI")
    print("=" * 50)
    runner.run(SuiteEncje.pobierz())

    print("\n" + "=" * 50)
    print("URUCHAMIANIE ZESTAWU: WARSTWA KONTROLI")
    print("=" * 50)
    runner.run(SuiteKontrola.pobierz())

    print("\n" + "=" * 50)
    print("URUCHAMIANIE ZESTAWU: TAGOWANE - KRYTYCZNE (Include)")
    print("=" * 50)
    runner.run(SuiteKrytyczne.pobierz())

    print("\n" + "=" * 50)
    print("URUCHAMIANIE ZESTAWU: TAGOWANE - PODSTAWOWE (Exclude)")
    print("=" * 50)
    runner.run(SuitePodstawowe.pobierz())