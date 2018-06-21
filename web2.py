from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
import urllib
import os

app = Flask(__name__)

@app.route('/api/v1/filmes', methods=['GET'])
def filmes():
    html_doc = urllib.urlopen("https://www.cinesystem.com.br/cinemas/rio-anil-shopping/856").read()
    soup = BeautifulSoup(html_doc, "html.parser")

    data = []
    for dataBox in soup.find_all("div", class_="col-md-12"):
        nomeObj = dataBox.find("h3", class_="nome-cinema").find('a')['href']
        #horariosObj = dataBox.find(class_="synopsis")
        data.append({
            'nome':nomeObj#//.text.strip()
        })

    return jsonify({ 'filmes': data})

if __name__ == '__main__':
    app.run(debug=True)
   # port = int(os.environ.get('PORT', 5000))
    #app.run(host='127.0.0.1', port=port)