from parameters import *
import psycopg2


class Boardgame:
	def __init__(self, name, id, age, description, minplayers, maxplayers, playingtime, image, typeBoladao, mechanics, categories):
		self.name = name
		self.id = id
		self.age = age
		self.description = str(description).replace("'", "")
		self.minplayers = minplayers
		self.maxplayers = maxplayers
		self.playingtime = playingtime
		self.image = image
		self.typeBoladao = typeBoladao
		self.mechanics = mechanics
		self.categories = categories


	def checkselfExists(self):
		conn = psycopg2.connect(connectionString)
		count = 0
		try:
			cur = conn.cursor()
			cmd =  "SELECT COUNT(*) FROM TB_BOARDGAME WHERE idbgg = %s" % (self.id)

			cur.execute(cmd)

			count = cur.fetchone() 

	    
		except (Exception, psycopg2.DatabaseError) as error:
			print(error)
		finally:
			if conn is not None:
				cur.close()
				conn.close()

		return count[0] > 0


	def save(self):
		try:
			conn = psycopg2.connect(connectionString)
			cur = conn.cursor()
			cmd = ""

			if not self.checkselfExists():
				cmd =  "INSERT INTO TB_BOARDGAME" \
					"(idbgg, name, age, description, minplayers, maxplayers, playingtime, image, idbggparent)" \
					" VALUES (%s, '%s', '%s', '%s', '%s', '%s', '%s', '%s', NULL )" % (
					self.id, self.name, self.age, self.description, self.minplayers, self.maxplayers, self.playingtime, self.image)
			else:
				print('existe')
				cmd =  "UPDATE TB_BOARDGAME SET " \
					"name = '%s', age  = '%s', description  = '%s', minplayers  = '%s', maxplayers  = '%s', playingtime  = '%s', image  = '%s' WHERE idbgg = %s" % (
					self.name, self.age, self.description, self.minplayers, self.maxplayers, self.playingtime, self.image, self.id)

			cur.execute(cmd)
			conn.commit()
	    
		except (Exception, psycopg2.DatabaseError) as error:
			print(error)
		finally:
			if conn is not None:
				cur.close()
				conn.close()


	