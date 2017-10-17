from os import getenv
from flask import Flask, Response
from model.cats import CatCollection
from service.api import APIService
 
app = Flask(__name__)

@app.route("/cat")
def get_cat():
	apisvc = APIService()
	cats = CatCollection()
	return Response(cats.insert(apisvc.getElementById("id"),
			    		apisvc.getElementById("url"),
		            		apisvc.getElementById("source_url")), status=200, mimetype='application/json')

@app.route("/history")
def get_history():
	cats = CatCollection()
	response = Response(cats.history(), status=200, mimetype='application/json')
	return response

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)
