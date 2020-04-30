import requests
import xml.etree.ElementTree as ET

class Boardgame:
	def __init__(self, name, id, age, description, minplayers, maxplayers, playingtime, typeBoladao, mechanics, categories):
		self.name = name
		self.id = id
		self.age = age
		self.description = description
		self.minplayers = minplayers
		self.maxplayers = maxplayers
		self.playingtime = playingtime
		self.typeBoladao = typeBoladao
		self.mechanics = mechanics
		self.categories = categories


def GameData(id, urlAPIGame):
	responseM = requests.get(urlAPIGame + str(id))
	treeM =  ET.ElementTree(ET.fromstring(responseM.content))
	
	mechanics = []
	categories = []
	bg = treeM.find("boardgame")
	name = bg.find('name').text
	age = bg.find('age').text
	minplayers = bg.find('minplayers').text
	maxplayers = bg.find('maxplayers').text
	playingtime = bg.find('playingtime').text



	typeBoladao = None if bg.find('boardgamesubdomain') is None else bg.find('boardgamesubdomain').text

	for mechanic in bg.findall("boardgamemechanic"):
		mechanics.append(mechanic.text)

	for category in bg.findall("boardgamecategory"):
		categories.append(category.text)

	description = None if bg.find('description') is None else bg.find('description').text
	return Boardgame(name, id, age, description, minplayers, maxplayers, playingtime, typeBoladao, mechanics, categories)


def GamesIOwn(urlAPIOwn, username):
	response = requests.get(urlAPIOwn + username)
	tree =  ET.ElementTree(ET.fromstring(response.content))

	return tree.findall("item")