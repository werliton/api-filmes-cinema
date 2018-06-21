from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import os

app = Flask(__name__)

@app.route('/api/v1/filmes', methods=['GET'])
def filmes():
    html_doc = urlopen("http://www.centerplex.com.br/programacao/cinema.php?cc=26").read()
    soup = BeautifulSoup(html_doc, "html.parser")

    data = []
    table = soup.select('table.tabelaprog')[0]
    for dataBox in table.find_all("a"):
        nomeObj = dataBox.get_text()
        #horariosObj = dataBox.find(class_="synopsis")
        data.append({
            'nome':nomeObj#.text.strip()
        })

    return jsonify({ 'filmes': data})

if __name__ == '__main__':
    app.run(debug=True)
   # port = int(os.environ.get('PORT', 5000))
    #app.run(host='127.0.0.1', port=port)