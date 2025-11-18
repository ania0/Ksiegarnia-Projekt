# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
# from Encje import Card
# from typing import List
#
# class AccessCard(Card):
# 	def __init__(self):
# 		self.___securityLevel = None
# 		self.___company = None

from encje import Card

class AccessCard(Card):
    def __init__(self):
        super().__init__()  # wywołanie konstruktora klasy bazowej
        self.___securityLevel: int = None
        self.___company: str = None
