from connHelper import *
from mechanic import *
from type import *
from category import *
import psycopg2


class Boardgame:
	def __init__(self, name, id, age, description, minplayers, maxplayers, playingtime, image, types, mechanics, categories):
		self.name = str(name).replace("'", "")
		self.id = id
		self.age = age
		self.description = str(description).replace("'", "")
		self.minplayers = minplayers
		self.maxplayers = maxplayers
		self.playingtime = playingtime
		self.image = image
		self.types = types
		self.mechanics = mechanics
		self.categories = categories

	def checkExists(self):
		
		cmd =  "SELECT COUNT(*) FROM TB_BOARDGAME WHERE idbgg = %s" % (self.id)
		count = executeSelectScalar(cmd)

		return count[0] > 0

	def save(self):
		
		cmd = ""
		if not self.checkExists():
			cmd =  "INSERT INTO TB_BOARDGAME" \
				"(idbgg, name, age, description, minplayers, maxplayers, playingtime, image, idbggparent)" \
				" VALUES (%s, '%s', '%s', '%s', '%s', '%s', '%s', '%s', NULL )" % (
				self.id, self.name, self.age, self.description, self.minplayers, self.maxplayers, self.playingtime, self.image)
		else:
			cmd =  "UPDATE TB_BOARDGAME SET " \
				"name = '%s', age  = '%s', description  = '%s', minplayers  = '%s', maxplayers  = '%s', playingtime  = '%s', image  = '%s' WHERE idbgg = %s" % (
				self.name, self.age, self.description, self.minplayers, self.maxplayers, self.playingtime, self.image, self.id)

		executeTransaction(cmd)
		self.saveMechanics()
		self.saveCategories()
		self.saveTypes()
		

	def saveMechanics(self):
		cmdDelete = "DELETE FROM TB_BOARDGAME_MECHANIC WHERE idbgg = %s" % (self.id)
		executeTransaction(cmdDelete)

		for mech in self.mechanics:
			mech.save()

			cmd =  "INSERT INTO TB_BOARDGAME_MECHANIC (idbgg, idmechanic) VALUES (%s, '%s')" % (self.id, mech.id)
			executeTransaction(cmd)


	def saveCategories(self):
		cmdDelete = "DELETE FROM TB_BOARDGAME_CATEGORY WHERE idbgg = %s" % (self.id)
		executeTransaction(cmdDelete)

		for categ in self.categories:
			categ.save()

			cmd =  "INSERT INTO TB_BOARDGAME_CATEGORY (idbgg, idcategory) VALUES (%s, '%s')" % (self.id, categ.id)
			executeTransaction(cmd)

	def saveTypes(self):
		cmdDelete = "DELETE FROM TB_BOARDGAME_TYPE WHERE idbgg = %s" % (self.id)
		executeTransaction(cmdDelete)

		for typ in self.types:
			typ.save()

			cmd =  "INSERT INTO TB_BOARDGAME_TYPE (idbgg, idType) VALUES (%s, '%s')" % (self.id, typ.id)
			executeTransaction(cmd)					