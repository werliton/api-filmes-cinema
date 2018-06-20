from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
import urllib
import os

app = Flask(__name__)

@app.route('/api/v1/filmes', methods=['GET'])
def filmes():
    html_doc = urllib.urlopen("http://www.adorocinema.com/filmes/numero-cinemas/").read()
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

if __name__ == '__main__':
    app.run(debug=True)
   # port = int(os.environ.get('PORT', 5000))
    #app.run(host='127.0.0.1', port=port)