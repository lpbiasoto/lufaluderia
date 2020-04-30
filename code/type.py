from parameters import *
from connHelper import *
import psycopg2


class Type:
	def __init__(self, id, description):
		self.id = id
		self.description = str(description).replace("'", "")
	
	def checkExists(self):
		
		cmd =  "SELECT COUNT(*) FROM TB_TYPE WHERE idtype = %s" % (self.id)
		count = executeSelectScalar(cmd)

		return count[0] > 0

	def save(self):
		
		cmd = ""
		if not self.checkExists():
			cmd =  "INSERT INTO TB_TYPE" \
				"(idtype, description) VALUES (%s, '%s')" % (self.id, self.description)
		else:
			cmd =  "UPDATE TB_TYPE SET description  = '%s' WHERE idtype= %s" % (self.description, self.id)

		executeTransaction(cmd)
