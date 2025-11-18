# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
# from Encje import Passenger
# from typing import List
#
# class MilesAccount(object):
# 	def __init__(self):
# 		self.___number : String = None
# 		self.___flightMiles : int = None
# 		self.___statusMiles : int = None
# 		self.___status : String = None
# 		self._unnamed_Passenger_ : Passenger = None
#


#!/usr/bin/python
# -*- coding: UTF-8 -*-

from encje.Passenger import Passenger
from typing import Optional

class MilesAccount:
    """
    Klasa reprezentująca konto milowe pasażera.
    """

    def __init__(self):
        self.__number: Optional[str] = None          # numer konta
        self.__flight_miles: int = 0                 # liczba mil za loty
        self.__status_miles: int = 0                 # liczba mil statusowych
        self.__status: Optional[str] = None          # status konta (np. Silver, Gold)
        self._passenger: Optional[Passenger] = None  # powiązany pasażer

