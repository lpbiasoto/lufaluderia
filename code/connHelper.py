import psycopg2
from parameters import *


def executeTransaction(cmd):
	try:
		conn = psycopg2.connect(connectionString)
		cur = conn.cursor()
		
		cur.execute(cmd)
		conn.commit()
    
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			cur.close()
			conn.close()



def executeSelectScalar(cmd):
	conn = psycopg2.connect(connectionString)
	result = 0
	try:
		cur = conn.cursor()
		cur.execute(cmd)
		result = cur.fetchone() 
    
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			cur.close()
			conn.close()

	return result