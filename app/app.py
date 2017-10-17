from os import getenv
from flask import Flask, Response, request
from model.cats import CatCollection
from service.api import APIService
 
app = Flask(__name__)

@app.route("/cat")
def get_cat():
	apisvc = APIService()
	cats = CatCollection()
	cats.insert(apisvc.getElementById("id"),
		apisvc.getElementById("url"),
		apisvc.getElementById("source_url"))

	response = Response(cats.latest(), status=200, mimetype='application/json')
	#response.headers['Link'] = "'" + request.host + "'" 
	return response

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)
