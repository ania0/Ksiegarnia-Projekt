#!/usr/bin/python
# -*- coding: UTF-8 -*-
# from abc import ABCMeta, abstractmethod
# from typing import List
#
# class ICena(object):
# 	"""@Interface"""
# 	__metaclass__ = ABCMeta
# 	@abstractmethod
# 	def obliczCene(self):
# 		pass


from abc import ABC, abstractmethod  # do tworzenia interf/klas abstrakt

# Klasy implementujące ten interfejs muszą dostarczyć metodę obliczCene().
class ICena(ABC):

    # met abstrakt - brak implementacji
    # każda kl dziedzicząca musi ją nadpisać
    @abstractmethod
    def obliczCene(self) -> float:
        pass

