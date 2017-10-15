from flask import Flask

app = Flask(__name__)

@app.route("/cat")
def get_cat():
	return "Meow!"

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)
