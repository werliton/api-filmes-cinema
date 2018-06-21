from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import os

app = Flask(__name__)

@app.route('/api/v1/copa/resultados')
def resultados():
    html_doc = urlopen("https://www.resultados.com/futebol/mundo/copa-do-mundo/resultados/").read()
    soup = BeautifulSoup(html_doc, "html.parser")

    data = []

    for dataBox in soup.find_all("tr",class_="odd stage-finished"):
        timcasa = dataBox.find('td', class_="cell_ab team bold").find("span")


        data.append({
            'timeCasa':timcasa.text.strip()
        })

    return jsonify({'resultados': data})

if __name__ == '__main__':
    app.run(debug=True)