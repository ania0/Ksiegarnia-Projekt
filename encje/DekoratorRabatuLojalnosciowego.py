# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
# from Encje import DekoraotrCenyZamowienia__klasa_Abstrakcyjna
# from typing import List
#
# class DekoratorRabatuLojalnosciowego(DekoraotrCenyZamowienia__klasa_Abstrakcyjna):
# 	pass


from encje.DekoratorCenyZamowienia__klasa_Abstrakcyjna import DekoratorCenyZamowienia  # import abstrakcyjnego dekoratora
from encje.Klient import Klient  # import klasy Klient – potrzebne do sprawdzenia lojalności



# dziedziczy po DekoratorCenyZamowienia, musi zaimplementować obliczCene()
class DekoratorRabatuLojalnosciowego(DekoratorCenyZamowienia):

    def obliczCene(self) -> float:
        # pobranie ceny bazowej z dekor komponent
        cena = self._komponent.obliczCene()

        # pobranie atrybut 'uzytkownik' z komponent
        # getattr - unik błędu jeśli atryb nie ma
        uzytkownik = getattr(self._komponent, 'uzytkownik', None)

        # Sprawdz czy uzytkownik jest instancją klasy Klient i czy klientLojalny == True
        if isinstance(uzytkownik, Klient) and uzytkownik.klientLojalny:
            cena *= 0.9  # zastosowanie 10% rabatu dla lojalnego klienta

        return cena
