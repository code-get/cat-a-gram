from os import getenv
from psycopg2 import connect, OperationalError

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
	dbname = ""
	dbuser = ""

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

		#save to database
		try:
			dbconn = connect("host=" + self.dbhost + " dbname=" + self.dbname + " user=" + self.dbuser + " password=" + self.dbpass)
			cur = dbconn.cursor()
		
			# I would never do this in real life do database update
			# this is could be a potential vulnerability
			# I would setup a broker table with a trigger to do the update or insert
			cur.execute("INSERT INTO image (id, url, source_url) VALUES ('"+ id + "', '" + url + "', '" + sourceUrl + "')")
			dbconn.commit() 
			cur.close()			
			dbconn.close()
		except OperationalError as err:
			raise err

	def __str__(self):
		outstr = ""
		for cat in self.cats:
			outstr += str(cat)
		return outstr	
