from func import *
from postgreConn import *
from parameters import *
from boardgame import *
import requests
import xml.etree.ElementTree as ET



list = []
listGames = GamesIOwn(urlAPIOwn, username)

# for child in listGames:
# 	id = child.attrib['objectid']
# 	list.append(GameData(id, urlAPIGame))


child = listGames[0]
id = child.attrib['objectid']
list.append(GameData(id, urlAPIGame))

list[0].save()