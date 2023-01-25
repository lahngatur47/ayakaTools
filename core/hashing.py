import numpy
import _sha1


class DATA:
	def __init__(self, run = True):
		self.HASH = None
		
	def hash16(self, Data, Data_arial_is = True):
		if Data_arial_is is True:
			list_Data_Arial = Data.split()
			
		
		else:
			return "data arial is false"