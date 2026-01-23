import sys
import os

# NAPRAWA ŚCIEŻEK
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

try:
    from encje.KsiazkaDAO import KsiazkaDAO
    from encje.UzytkownikDAO import UzytkownikDAO
    from encje.ZamowienieDAO import ZamowienieDAO
    from encje.FabrykaKsiazek import FabrykaKsiazek
    from encje.DekoratorRabatuLojalnosciowego import DekoratorRabatuLojalnosciowego
    from encje.FasadaEncji import FasadaEncji
    from kontrola.KsiegarniaKontrolaFacade import KsiegarniaKontrolaFacade

except ImportError as e:
    print(f"\n[CRITICAL ERROR] Nie udało się zaimportować modułów.")
    print(f"Sprawdź czy pliki DAO istnieją w folderze 'encje'.")
    print(f"Szczegóły: {e}\n")
    raise e


class SetUp:
    """
    Singleton - stan aplikacji w pamięci
    """
    Inwentarz = None  # Fasada Encji (do weryfikacji)
    Kontrola = None  # Fasada Kontroli (punkt wejscia testów)

    def __init__(self):
        # inicjalizacja systemu tylko raz
        if SetUp.Kontrola is None:
            self._zainicjuj_system()

    def _zainicjuj_system(self):
        print("--- [SETUP] Tworzenie obiektów DAO i Fasad ---")

        dao_ksiazki = KsiazkaDAO()
        dao_uzytkownicy = UzytkownikDAO()
        dao_zamowienia = ZamowienieDAO()
        fabryka = FabrykaKsiazek()
        dekorator = DekoratorRabatuLojalnosciowego

        # DAO do Fasady Encji
        SetUp.Inwentarz = FasadaEncji(
            dao_ksiazki,
            dao_uzytkownicy,
            dao_zamowienia,
            fabryka,
            dekorator
        )

        # Fasada Encji do Fasady Kontroli
        SetUp.Kontrola = KsiegarniaKontrolaFacade(SetUp.Inwentarz)