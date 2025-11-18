#!/usr/bin/python
# -*- coding: UTF-8 -*-
from encje.MilesCard import MilesCard
from encje.MilesAccount import MilesAccount
from typing import List

class Passenger(object):
	def creditMiles(self, aB : Fasada):
		pass

	def consumeMiles(self, aB : Fasada):
		pass

	def cancelMiles(self):
		pass

	def __init__(self, name: str = None, mileCard: MilesCard = None, status: str = None):
		self.name = name
		self.mileCard = mileCard  # composition: Passenger "posiada" MileCard
		self.status = status
		self.milesAccount = MilesAccount()  # optional, można też przekazać jako parametr




