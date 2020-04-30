import requests
import ast
import xml.etree.ElementTree as ET
from boardgame import *

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
	image = bg.find('image').text

	print(image)




	typeBoladao = None if bg.find('boardgamesubdomain') is None else bg.find('boardgamesubdomain').text

	for mechanic in bg.findall("boardgamemechanic"):
		mechanics.append(mechanic.text)

	for category in bg.findall("boardgamecategory"):
		categories.append(category.text)

	description = None if bg.find('description') is None else bg.find('description').text
	return Boardgame(name, id, age, description, minplayers, maxplayers, playingtime, image, typeBoladao, mechanics, categories)


def GamesIOwn(urlAPIOwn, username):
	response = requests.get(urlAPIOwn + username)
	tree =  ET.ElementTree(ET.fromstring(response.content))

	return tree.findall("item")