from connHelper import *

class Category:
	def __init__(self, id, description):
		self.id = id
		self.description = str(description).replace("'", "")
	
	def checkExists(self):
		
		cmd =  "SELECT COUNT(*) FROM TB_CATEGORY WHERE idcategory = %s" % (self.id)
		count = executeSelectScalar(cmd)

		return count[0] > 0

	def save(self):
		cmd = ""
		if not self.checkExists():
			cmd =  "INSERT INTO TB_CATEGORY" \
				"(idcategory, description) VALUES (%s, '%s')" % (self.id, self.description)
		else:
			cmd =  "UPDATE TB_CATEGORY SET description  = '%s' WHERE idcategory= %s" % (self.description, self.id)
		
		executeTransaction(cmd)
			