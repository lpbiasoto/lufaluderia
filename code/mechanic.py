from parameters import *
from connHelper import *
import psycopg2


class Mechanic:
	def __init__(self, id, description):
		self.id = id
		self.description = str(description).replace("'", "")
	
	def checkExists(self):

		cmd =  "SELECT COUNT(*) FROM TB_MECHANIC WHERE idmechanic = %s" % (self.id)
		count = executeSelectScalar(cmd)
		
		return count[0] > 0

	def save(self):
		
		cmd = ""
		if not self.checkExists():
			cmd =  "INSERT INTO TB_MECHANIC" \
				"(idmechanic, description) VALUES (%s, '%s')" % (self.id, self.description)
		else:
			cmd =  "UPDATE TB_MECHANIC SET description  = '%s' WHERE idmechanic = %s" % (self.description, self.id)

		executeTransaction(cmd)
		