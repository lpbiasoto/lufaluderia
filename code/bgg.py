from func import *
from parameters import *
from boardgame import *
import xml.etree.ElementTree as ET



list = []
listGames = GamesIOwn(urlAPIOwn, username)

for child in listGames:
	id = child.attrib['objectid']
	GameData(id, urlAPIGame).save()
