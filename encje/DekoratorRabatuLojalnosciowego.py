# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
# from Encje import DekoraotrCenyZamowienia__klasa_Abstrakcyjna
# from typing import List
#
# class DekoratorRabatuLojalnosciowego(DekoraotrCenyZamowienia__klasa_Abstrakcyjna):
# 	pass


from encje.DekoratorCenyZamowienia__klasa_Abstrakcyjna import DekoratorCenyZamowienia
from encje.Klient import Klient
from encje.Zamowienie import Zamowienie

class DekoratorRabatuLojalnosciowego(DekoratorCenyZamowienia):
    def obliczCene(self) -> float:
        cena = self._komponent.obliczCene()
        uzytkownik = getattr(self._komponent, 'uzytkownik', None)

        if isinstance(uzytkownik, Klient) and uzytkownik.klientLojalny:
            cena *= 0.9  # 10% rabatu dla lojalnego klienta
        return cena
