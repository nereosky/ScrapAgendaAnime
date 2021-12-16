from flask import Flask,render_template, jsonify, request , make_response
from jinja2 import Template
import scrap

import os


app = Flask(__name__)
port = int(os.environ.get("PORT",5000))

indexLink = "Accueil"

@app.route('/')
def index():
    animeList = "animeList"    
    return render_template("index.html", anime_list = animeList)

@app.route('/animelist', methods=['GET'])
def read():
    
    jourDict = scrap.scrapAgenda()

    return render_template("animelist.html", index_link = indexLink, jour_dict = jourDict)


@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error':'Not Found'}),404)

if __name__ == "__main__":        
    # app.run(debug=True,host='127.0.0.1',port = port) #local
	app.run(host = "0.0.0.0", port = port, debug=True) #container  