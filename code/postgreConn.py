import psycopg2
from func import *

def insertBG(bg):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect("dbname='lufaluderia' user='bg' host='192.168.0.109' password='neverlevis'")

        # create a cursor
        cur = conn.cursor()
        insertCommand =  "INSERT INTO TB_BOARDGAME" \
            "(idbgg, name, age, description, minplayers, maxplayers, playingtime, image, idbggparent)" \
            " VALUES (%s, '%s', '%s', '%s', '%s', '%s', '%s', '', NULL )" % (
            bg.id, bg.name, bg.age, bg.description, bg.minplayers, bg.maxplayers, bg.playingtime)

        print(insertCommand)



    	# execute a statement
        print('PostgreSQL database version:')
        cur.execute(insertCommand)

        conn.commit()
        cur.close()
        
    except (Exception, psycopg2.DatabaseError) as error:
        print('OI')
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
