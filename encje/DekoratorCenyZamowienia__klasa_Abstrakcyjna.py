# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
# from Encje import ICena
# from typing import List
#
# class DekoraotrCenyZamowienia__klasa_Abstrakcyjna(object):
# 	"""Abstrakcyjna klasa"""
# 	def __init__(self):
# 		self._unnamed_ICena_ : ICena = None

from encje.ICena import ICena  # import interfejsu ICena
from abc import ABC, abstractmethod  # import do tworzenia klas abstrakcyjnych

# dziedziczy po ICena oraz po ABC
class DekoratorCenyZamowienia(ICena, ABC):

    def __init__(self, komponent: ICena):
        # przechowujemy obiekt, który dekorujemy - rozszerzyć jego działanie
        self._komponent: ICena = komponent

    @abstractmethod  # met abstrakt – musi zostać nadpisana w kl potomnych
    def obliczCene(self) -> float:
        pass
