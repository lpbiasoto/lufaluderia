import requests
import xml.etree.ElementTree as ET

class Boardgame:
	def __init__(self, name, id, mechanics, typeBoladao):
		self.name = name
		self.id = id
		self.typeBoladao = typeBoladao
		self.mechanics = mechanics
		self.category = []


def GameData(id, urlAPIGame):
	responseM = requests.get(urlAPIGame + str(id))
	treeM =  ET.ElementTree(ET.fromstring(responseM.content))
	
	mechanics = []
	bg = treeM.find("boardgame")
	name = bg.find('name').text

	print(id, bg.find('boardgamesubdomain'))
	typeBoladao = "" if bg.find('boardgamesubdomain') is None else bg.find('boardgamesubdomain').text

	for mechanic in bg.findall("boardgamemechanic"):
		mechanics.append(mechanic.text)


	return Boardgame(name, id, mechanics, typeBoladao)


def GamesIOwn(urlAPIOwn, username):
	response = requests.get(urlAPIOwn + username)
	tree =  ET.ElementTree(ET.fromstring(response.content))

	return tree.findall("item")