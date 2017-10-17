from os import getenv
from psycopg2 import connect, OperationalError
from json import dumps

class CatCollection:
	def insert(self, id, url, sourceUrl):
		#save to database
		try:
			dbconn = connect("host=" + getenv("DB_HOST") + " dbname=" + getenv("DB_NAME") + " user=" + getenv("DB_USER") + " password=" + getenv("DB_PASSWORD"))
			cur = dbconn.cursor()
			#NOTE: this direct insert is just for simplicity I would normally setup a broker table with a trigger to do the update or insert
			cur.execute("INSERT INTO image (id, url, source_url) VALUES ('"+ id + "', '" + url + "', '" + sourceUrl + "')")
			dbconn.commit() 
			cur.close()			
			dbconn.close()
		except OperationalError as err:
			raise err

		return dumps({'image': {'url': "'" + url + "'", 'id': "'" + id + "'", 'source_url': "'" + sourceUrl + "'" }})

	def history(self):
		outstr = {}
		outstr['images'] = []
		try:
			dbconn = connect("host=" + getenv("DB_HOST") + " dbname=" + getenv("DB_NAME") + " user=" + getenv("DB_USER") + " password=" + getenv("DB_PASSWORD"))
			cur = dbconn.cursor()
			cur.execute("SELECT id, url, source_url FROM image;")
			records = cur.fetchall()
			recordCount = 0
			for record in records:
				catimage = {}
				catimage['url'] = record[1]
				catimage['id'] = record[0]
				catimage['source_url'] = record[2]
				outstr['images'] += [catimage]
			cur.close()
			dbconn.close()
		except OperationalError as err:
			raise err

		return dumps(outstr)	
