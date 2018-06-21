from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import os

app = Flask(__name__)

@app.route('/api/v1/copa/resultados')
def resultados():
    html_doc = urlopen("http://upcuesta.com.br/portal/2018/06/21/copa-do-mundo-2018-tabela-de-jogos/").read()
    soup = BeautifulSoup(html_doc, "html.parser")

    data = []
    
    for dataBox in soup.find_all("tr"):
        for tdBox in dataBox.find_all('td',{'width':'194'}):
            jogos = tdBox.text
            data.append({
                'jogos':jogos.strip()
            })

    return jsonify({'resultados': data})

if __name__ == '__main__':
    app.run(debug=True)