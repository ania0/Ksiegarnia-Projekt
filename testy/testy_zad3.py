import unittest
from test_ebook import TestEbook
from test_ksiazka_papierowa import TestKsiazkaPapierowa
from test_uzytkownik import TestUzytkownik
from test_zamowienie import TestZamowienie
from testy_zad2 import TestKsiegarniaKontrolaMock

class SuiteHelper:
    @staticmethod
    def filtruj_testy(zestaw_wejsciowy, include=None, exclude=None):
        nowy_zestaw = unittest.TestSuite()
        for test in zestaw_wejsciowy:
            if isinstance(test, unittest.TestSuite):
                podzestaw = SuiteHelper.filtruj_testy(test, include, exclude)
                if podzestaw.countTestCases() > 0:
                    nowy_zestaw.addTest(podzestaw)
            else:
                metoda = getattr(test, test._testMethodName)
                tagi_metody = getattr(metoda, 'tags', set())

                if include and not (set(include) & tagi_metody):
                    continue
                if exclude and (set(exclude) & tagi_metody):
                    continue

                nowy_zestaw.addTest(test)
        return nowy_zestaw


# ZESTAWY TESTOW

class SuiteEncje:

    @staticmethod
    def pobierz():
        suite = unittest.TestSuite()
        loader = unittest.TestLoader()
        suite.addTests(loader.loadTestsFromTestCase(TestEbook))
        suite.addTests(loader.loadTestsFromTestCase(TestKsiazkaPapierowa))
        suite.addTests(loader.loadTestsFromTestCase(TestUzytkownik))
        suite.addTests(loader.loadTestsFromTestCase(TestZamowienie))
        return suite


class SuiteKontrola:

    @staticmethod
    def pobierz():
        loader = unittest.TestLoader()
        return loader.loadTestsFromTestCase(TestKsiegarniaKontrolaMock)


class SuiteKrytyczne:

    @staticmethod
    def pobierz():
        loader = unittest.TestLoader()
        wszystkie = unittest.TestSuite([
            loader.loadTestsFromTestCase(TestEbook),
            loader.loadTestsFromTestCase(TestKsiazkaPapierowa),
            loader.loadTestsFromTestCase(TestUzytkownik),
            loader.loadTestsFromTestCase(TestZamowienie),
            loader.loadTestsFromTestCase(TestKsiegarniaKontrolaMock)
        ])
        return SuiteHelper.filtruj_testy(wszystkie, include=["krytyczne"])


class SuitePodstawowe:

    @staticmethod
    def pobierz():
        loader = unittest.TestLoader()
        wszystkie = unittest.TestSuite([
            loader.loadTestsFromTestCase(TestUzytkownik),
            loader.loadTestsFromTestCase(TestZamowienie),
            loader.loadTestsFromTestCase(TestKsiegarniaKontrolaMock)
        ])
        return SuiteHelper.filtruj_testy(wszystkie, exclude=["zaawansowane", "bledy"])


# URUCHAMIANIE WSZYSTKIEGO

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)

    print("URUCHAMIANIE ZESTAWU: WARSTWA ENCJI")
    runner.run(SuiteEncje.pobierz())

    print("URUCHAMIANIE ZESTAWU: WARSTWA KONTROLI")
    runner.run(SuiteKontrola.pobierz())

    print("URUCHAMIANIE ZESTAWU: KRYTYCZNE ")
    runner.run(SuiteKrytyczne.pobierz())

    print("URUCHAMIANIE ZESTAWU: PODSTAWOWE ")
    runner.run(SuitePodstawowe.pobierz())