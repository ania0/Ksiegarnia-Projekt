# from encje.DekoratorCenyZamowienia__klasa_Abstrakcyjna import DekoratorCenyZamowienia  # import abstrakcyjnego dekoratora
# from encje.Klient import Klient  # import klasy Klient – potrzebne do sprawdzenia lojalności
#
#
#
# # dziedziczy po DekoratorCenyZamowienia, musi zaimplementować obliczCene()
# class DekoratorRabatuLojalnosciowego(DekoratorCenyZamowienia):
#
#     def obliczCene(self) -> float:
#         # pobranie ceny bazowej z dekor komponent
#         cena = self._komponent.obliczCene()
#
#         # pobranie uzytkownika z komponent
#         uzytkownik = self._komponent.pobierzKlienta()
#
#         # Sprawdz czy uzytkownik jest instancją klasy Klient i czy klientLojalny == True
#         if isinstance(uzytkownik, Klient) and uzytkownik.klientLojalny:
#             cena *= 0.9  # zastosowanie 10% rabatu dla lojalnego klienta
#
#         return cena

from encje.DekoratorCenyZamowienia import DekoratorCenyZamowienia

from encje.Klient import Klient


class DekoratorRabatuLojalnosciowego(DekoratorCenyZamowienia):
    """
    Dekorator rabatu lojalnościowego.
    Na tym etapie zawiera tylko sygnaturę metody oraz zwraca testową wartość.
    """

    def obliczCene(self) -> float:
        print("DekoratorRabatuLojalnosciowego: obliczCene() – tymczasowa implementacja.")
        raise NotImplementedError()

    def pobierzKlienta(self) -> Klient:
        print("DekoratorRabatuLojalnosciowego: pobierzKlienta() – tymczasowa implementacja.")
        raise NotImplementedError()


