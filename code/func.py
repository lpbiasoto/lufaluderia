import requests
import ast
import xml.etree.ElementTree as ET
from boardgame import *
from mechanic import *
from type import *
from category import *

def GameData(id, urlAPIGame):
	responseM = requests.get(urlAPIGame + str(id))
	treeM =  ET.ElementTree(ET.fromstring(responseM.content))
	
	mechanics = []
	categories = []
	types = []
	bg = treeM.find("boardgame")
	name = ""
	
	
	for f in bg.findall('name'):

		if 'primary' in f.attrib and f.attrib['primary'] == "true":
			name = f.text
			break

	print(name)
	#name = [f for f in bg.findall('name') if f.attrib['primary']  == True][0]
	#name = bg.find('name').text
	age = bg.find('age').text
	minplayers = bg.find('minplayers').text
	maxplayers = bg.find('maxplayers').text
	playingtime = bg.find('playingtime').text
	image = bg.find('image').text
	description = None if bg.find('description') is None else bg.find('description').text
	
	for type in bg.findall("boardgamesubdomain"):
		typ = Type(type.attrib['objectid'] , type.text)
		types.append(typ)

	for mechanic in bg.findall("boardgamemechanic"):
		mech = Mechanic(mechanic.attrib['objectid'] , mechanic.text)
		mechanics.append(mech)

	for category in bg.findall("boardgamecategory"):
		cate = Category(category.attrib['objectid'] , category.text)
		categories.append(cate)

	
	return Boardgame(name, id, age, description, minplayers, maxplayers, playingtime, image, types, mechanics, categories)


def GamesIOwn(urlAPIOwn, username):
	response = requests.get(urlAPIOwn + username)
	tree =  ET.ElementTree(ET.fromstring(response.content))

	return tree.findall("item")