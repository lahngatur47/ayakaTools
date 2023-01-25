import sys
import string
import datetime as dt
class INIT:
	def __init__(self):
		self.MESSAGE = "none"
		self.HINT = 0
		self.DATE = None
		
	def req(self,data_arial:string , data_arial_is = True)->string :
		if data_arial_is == False:
			return None
		else:
			list_data_arial = data_arial.split()
			
		
		