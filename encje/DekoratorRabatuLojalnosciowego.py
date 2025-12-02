# from encje.DekoratorCenyZamowienia__klasa_Abstrakcyjna import DekoratorCenyZamowienia  # import abstrakcyjnego dekoratora
# from encje.Klient import Klient  # import klasy Klient – potrzebne do sprawdzenia lojalności
#
#
#
# # dziedziczy po DekoratorCenyZamowienia, musi zaimplementować obliczCene()
# class DekoratorRabatuLojalnosciowego(DekoratorCenyZamowienia):
#
#     def obliczCene(self) -> float:
#         # cena = self._komponent.obliczCene()
#         # klient = self.pobierzKlienta()
#         # if klient.klientLojalny: cena *= 0.9
#         return cena

from encje.DekoratorCenyZamowienia import DekoratorCenyZamowienia
from encje.Klient import Klient

class DekoratorRabatuLojalnosciowego(DekoratorCenyZamowienia):
    """
    Dekorator rabatu lojalnościowego.
    Na tym etapie zawiera tylko sygnaturę metody oraz zwraca testową wartość.
    """

    def obliczCene(self) -> float:
        baza = self._komponent.obliczCene()
        print(f">>> DekoratorRabatuLojalnosciowego: nakładam testowy rabat 10% na {baza}")
        return baza * 0.9