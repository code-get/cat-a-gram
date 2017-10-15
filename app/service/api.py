from os import getenv
from urllib.request import urlopen
from xml.dom.minidom import parseString

class APIService:
	dom = ""

	def __init__(self):
		with urlopen(getenv("API_URL")) as apihandle:
			 self.dom = parseString(apihandle.read())

	def getElementById(self, id):
		return str(self.dom.getElementsByTagName(id)[0].childNodes[0].data)
		
