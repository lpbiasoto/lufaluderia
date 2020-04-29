from func import *
import requests
import xml.etree.ElementTree as ET

urlAPIOwn = "https://www.boardgamegeek.com/xmlapi/collection/"
urlAPIGame = "https://www.boardgamegeek.com/xmlapi/boardgame/"
username = "fcarvalho"

list = []
listGames = GamesIOwn(urlAPIOwn, username)

for child in listGames:
	id = child.attrib['objectid']
	list.append(GameData(id, urlAPIGame))