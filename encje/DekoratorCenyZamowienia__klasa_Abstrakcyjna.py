# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
# from Encje import ICena
# from typing import List
#
# class DekoraotrCenyZamowienia__klasa_Abstrakcyjna(object):
# 	"""Abstrakcyjna klasa"""
# 	def __init__(self):
# 		self._unnamed_ICena_ : ICena = None

from encje.ICena import ICena
from abc import ABC, abstractmethod

class DekoratorCenyZamowienia(ICena, ABC):
    def __init__(self, komponent: ICena):
        self._komponent: ICena = komponent

    @abstractmethod
    def obliczCene(self) -> float:
        pass
