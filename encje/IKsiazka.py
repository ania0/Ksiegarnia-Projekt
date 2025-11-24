#!/usr/bin/python
# -*- coding: UTF-8 -*-
# from abc import ABCMeta, abstractmethod
from typing import List

# class iKsiazka(object):
# 	"""@Interface"""
# 	__metaclass__ = ABCMeta
# 	pass

from abc import ABC, abstractmethod  # import ABC i abstractmethod do tworzenia interfejsów


# Interf reprezentujący książkę
# Każda kl implementująca IKsiazka musi dostarczyć met
class IKsiazka(ABC):

    @abstractmethod
    def pobierzCene(self) -> float:
        pass
