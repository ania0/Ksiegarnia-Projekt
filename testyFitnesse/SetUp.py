import sys
import os

# Ustawienie ścieżki, aby widział foldery 'encje' i 'kontrola'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from encje.FasadaEncji import FasadaEncji
from encje.UzytkownikDAO import UzytkownikDAO
from encje.KsiazkaDAO import KsiazkaDAO
from encje.ZamowienieDAO import ZamowienieDAO
from encje.FabrykaKsiazek import FabrykaKsiazek
from encje.DekoratorRabatuLojalnosciowego import DekoratorRabatuLojalnosciowego
from kontrola.KsiegarniaKontrolaFacade import KsiegarniaKontrolaFacade


class SetUp:
    Inwentarz = None
    PU = None

    def __init__(self):
        # 1. Inicjalizacja DAO
        u_dao = UzytkownikDAO()
        k_dao = KsiazkaDAO()
        z_dao = ZamowienieDAO()

        # 2. Narzędzia
        fabryka = FabrykaKsiazek()
        rabat = DekoratorRabatuLojalnosciowego

        # 3. Fasada Encji (Inwentarz)
        SetUp.Inwentarz = FasadaEncji(k_dao, u_dao, z_dao, fabryka, rabat)

        # 4. Fasada Kontroli
        SetUp.PU = KsiegarniaKontrolaFacade(SetUp.Inwentarz)


# Inicjalizacja instancji przy imporcie
setup_instance = SetUp()