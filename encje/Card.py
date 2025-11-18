# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
# from abc import ABCMeta, abstractmethod
# from typing import List
#
# class Card(object):
# 	__metaclass__ = ABCMeta
# 	@classmethod
# 	def checkValidity(self):
# 		pass
#
# 	@classmethod
# 	def __init__(self):
# 		self.___owner = None
# 		self.___number : String = None
# 		self.___validUntil = None
#


from abc import ABC, abstractmethod

class Card(ABC):
    def __init__(self):
        self.___owner = None
        self.___number: str = None
        self.___validUntil = None

    @abstractmethod
    def checkValidity(self) -> bool:
        pass
