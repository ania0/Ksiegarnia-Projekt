import sys
import os

# ========================================================
# 1. NAPRAWA ŚCIEŻEK (ABSOLUTNIE KONIECZNE NA GÓRZE)
# ========================================================
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

# ========================================================
# 2. IMPORTY KLAS (TWOJE RZECZYWISTE PLIKI)
# ========================================================
try:
    # WARSTWA DANYCH (DAO zamiast Repozytoriow)
    from encje.KsiazkaDAO import KsiazkaDAO
    from encje.UzytkownikDAO import UzytkownikDAO
    from encje.ZamowienieDAO import ZamowienieDAO

    # WARSTWA LOGIKI BIZNESOWEJ
    from encje.FabrykaKsiazek import FabrykaKsiazek
    from encje.DekoratorRabatuLojalnosciowego import DekoratorRabatuLojalnosciowego
    from encje.FasadaEncji import FasadaEncji

    # WARSTWA KONTROLI (Fasada, którą testujemy)
    from kontrola.KsiegarniaKontrolaFacade import KsiegarniaKontrolaFacade

except ImportError as e:
    print(f"\n[CRITICAL ERROR] Nie udało się zaimportować modułów.")
    print(f"Sprawdź czy pliki DAO istnieją w folderze 'encje'.")
    print(f"Szczegóły: {e}\n")
    raise e


class SetUp:
    """
    Singleton trzymający stan całej aplikacji w pamięci na czas testów.
    """
    Inwentarz = None  # Fasada Encji (tzw. Backdoor do weryfikacji)
    Kontrola = None  # Fasada Kontroli (Główny punkt wejścia testów)

    def __init__(self):
        # Inicjalizujemy system tylko raz
        if SetUp.Kontrola is None:
            self._zainicjuj_system()

    def _zainicjuj_system(self):
        print("--- [SETUP] Tworzenie obiektów DAO i Fasad ---")

        # 1. Tworzymy konkretne implementacje (DAO)
        dao_ksiazki = KsiazkaDAO()
        dao_uzytkownicy = UzytkownikDAO()
        dao_zamowienia = ZamowienieDAO()

        # 2. Obiekty pomocnicze
        fabryka = FabrykaKsiazek()
        dekorator = DekoratorRabatuLojalnosciowego

        # 3. Wstrzykujemy DAO do Fasady Encji
        # (Kolejność argumentów musi zgadzać się z __init__ w FasadaEncji!)
        SetUp.Inwentarz = FasadaEncji(
            dao_ksiazki,  # repoKsiazek
            dao_uzytkownicy,  # repoUzytkownika
            dao_zamowienia,  # repoZamowien
            fabryka,
            dekorator
        )

        # 4. Wstrzykujemy Fasadę Encji do Fasady Kontroli
        SetUp.Kontrola = KsiegarniaKontrolaFacade(SetUp.Inwentarz)