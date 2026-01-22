import sys
import os

# Dodajemy ścieżkę do katalogu nadrzędnego, aby Python widział 'encje' i 'kontrola'
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

# Importy klas z Twojego projektu
from encje.UzytkownikDAO import UzytkownikDAO
from encje.KsiazkaDAO import KsiazkaDAO
from encje.ZamowienieDAO import ZamowienieDAO
from encje.FabrykaKsiazek import FabrykaKsiazek
from encje.DekoratorRabatuLojalnosciowego import DekoratorRabatuLojalnosciowego
from encje.FasadaEncji import FasadaEncji
from kontrola.KsiegarniaKontrolaFacade import KsiegarniaKontrolaFacade


class SetUp:
    # Zmienne statyczne (Singleton dla testów)
    Inwentarz = None  # Odpowiednik 'encje_fasada'
    Kontrola = None  # Odpowiednik 'fasada_kontroli'

    def __init__(self):
        pass


# Inicjalizacja (logika skopiowana z main.py)
if SetUp.Inwentarz is None:
    # 1. Tworzymy DAO
    uzytkownik_dao = UzytkownikDAO()
    ksiazka_dao = KsiazkaDAO()
    zamowienie_dao = ZamowienieDAO()

    # 2. Obiekty pomocnicze
    fabryka_ksiazek = FabrykaKsiazek()
    dekorator_rabatu = DekoratorRabatuLojalnosciowego

    # 3. Tworzymy FASADĘ ENCJI
    SetUp.Inwentarz = FasadaEncji(
        repoKsiazek=ksiazka_dao,
        repoUzytkownika=uzytkownik_dao,
        repoZamowien=zamowienie_dao,
        fabrykaKsiazek=fabryka_ksiazek,
        dekoratorRabatu=dekorator_rabatu
    )

    # 4. Tworzymy FASADĘ KONTROLI
    SetUp.Kontrola = KsiegarniaKontrolaFacade(encje_fasada=SetUp.Inwentarz)