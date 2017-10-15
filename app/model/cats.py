from psycopg2 import connect

class CatImage:
	url = ""
	id = ""
	sourceUrl = ""

	def __init__(self, id, url, sourceUrl):
		self.id = id
		self.url = url
		self.sourceUrl = sourceUrl

	def getUrl(self):
		return self.url

	def getId(self):
		return self.id

	def getSourceUrl(self):
		return self.sourceUrl

	def __str__(self):
		return self.id + ":" + self.url + ":" + self.sourceUrl + "\n"

class CatCollection:
	cats = ""

	def __init__(self):
		self.cats = []

	def insert(self, id, url, sourceUrl):
		cat = CatImage(id, url, sourceUrl)
		#save to database
		self.cats += [cat]

	def __str__(self):
		outstr = ""
		for cat in self.cats:
			outstr += str(cat)
		return outstr	
