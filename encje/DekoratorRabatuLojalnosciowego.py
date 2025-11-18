# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
# from Encje import DekoraotrCenyZamowienia__klasa_Abstrakcyjna
# from typing import List
#
# class DekoratorRabatuLojalnosciowego(DekoraotrCenyZamowienia__klasa_Abstrakcyjna):
# 	pass


from encje.DekoratorCenyZamowienia__klasa_Abstrakcyjna import DekoratorCenyZamowienia
from encje.Klient import Klient

class DekoratorRabatuLojalnosciowego(DekoratorCenyZamowienia):
    def obliczCene(self) -> float:
        cena = self._zamowienie.obliczCene()
        if isinstance(self._zamowienie.uzytkownik, Klient) and self._zamowienie.uzytkownik.KlientLojalny:
            cena *= 0.9  # 10% rabatu dla lojalnego klienta
        return cena
