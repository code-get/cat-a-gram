from os import getenv
from psycopg2 import connect, OperationalError
from json import dumps

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
		return dumps({'image': {'url': "'" + self.url + "'", 'id': "'" + self.id + "'", 'source_url': "'" + self.sourceUrl + "'" }})

class CatCollection:
	cats = ""
	lastcat = ""

	def __init__(self):
		self.cats = []
		self.dbhost = getenv("DB_HOST")
		self.dbname = getenv("DB_NAME")
		self.dbuser = getenv("DB_USER")
		self.dbpass = getenv("DB_PASSWORD")

	def insert(self, id, url, sourceUrl):
		cat = CatImage(id, url, sourceUrl)
		
		#save to collection
		self.cats += [cat]
		self.lastcat = cat

		#save to database
		try:
			dbconn = connect("host=" + self.dbhost + " dbname=" + self.dbname + " user=" + self.dbuser + " password=" + self.dbpass)
			cur = dbconn.cursor()
			#NOTE: this direct insert is just for simplicity I would normally setup a broker table with a trigger to do the update or insert
			cur.execute("INSERT INTO image (id, url, source_url) VALUES ('"+ id + "', '" + url + "', '" + sourceUrl + "')")
			dbconn.commit() 
			cur.close()			
			dbconn.close()
		except OperationalError as err:
			raise err

	def latest(self):
		return str(self.lastcat)	

	def __str__(self):
		outstr = ""
		for cat in self.cats:
			outstr += str(cat)
		return outstr	
