# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
# from Encje import Passenger
# from Encje import Card
# from typing import List
#
# class MilesCard(Card):
# 	def __init__(self):
# 		self.___status : String = None
# 		self._unnamed_Passenger_ : Passenger = None
#


#!/usr/bin/python
# -*- coding: UTF-8 -*-

from encje.Passenger import Passenger
from encje.Card import Card
from typing import Optional

class MilesCard(Card):
    """
    Klasa reprezentująca kartę milową pasażera.
    Dziedziczy po klasie Card.
    """

    def __init__(self):
        super().__init__()  # wywołanie konstruktora klasy bazowej
        self.__status: Optional[str] = None
        self._passenger: Optional[Passenger] = None  # powiązanie z pasażerem

