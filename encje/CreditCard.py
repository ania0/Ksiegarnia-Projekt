# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
# from Encje import Card
# from typing import List
#
# class CreditCard(Card):
# 	def __init__(self):
# 		self.___validFrom : String = None
# 		self.___controlNumber : int = None
#


from encje import Card
class CreditCard(Card):
    def __init__(self):
        self.__validFrom: str = None
        self.__controlNumber: int = None