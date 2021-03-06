from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import os

app = Flask(__name__)
api = Api(app)

class Filmes(Resource):
    def get(self):
        html_doc = urlopen("http://www.adorocinema.com/filmes/numero-cinemas/").read()
        soup = BeautifulSoup(html_doc, "html.parser")

        data = []
        for dataBox in soup.find_all("div", class_="card card-entity card-entity-list cf"):
            nomeObj = dataBox.find("h2", class_="meta-title").find("a", class_="meta-title-link")
            imgObj  = dataBox.find(class_="thumbnail")
            sinopseObj = dataBox.find(class_="synopsis")
            dataObj = dataBox.find("span", class_="date")
            data.append({
                'nome':nomeObj.text.strip(),
                'poster':imgObj.img['src'].strip(),
                'sinopse': sinopseObj.text.strip(),
                'data': dataObj.text.strip()
            })

        return jsonify({ 'filmes': data})

api.add_resource(Filmes, "/api/v1/filmes")

if __name__ == '__main__':
    #app.run()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)