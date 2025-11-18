#!/usr/bin/python
# -*- coding: UTF-8 -*-
# from abc import ABCMeta, abstractmethod
from typing import List

# class iKsiazka(object):
# 	"""@Interface"""
# 	__metaclass__ = ABCMeta
# 	pass

from abc import ABC, abstractmethod

class IKsiazka(ABC):
    @abstractmethod
    def pobierzCene(self) -> float:
        pass
