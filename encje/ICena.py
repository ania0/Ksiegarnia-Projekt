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

from abc import ABC, abstractmethod

class ICena(ABC):
    @abstractmethod
    def obliczCene(self) -> float:
        pass
