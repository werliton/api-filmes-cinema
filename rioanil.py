from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import os

app = Flask(__name__)

@app.route('/api/v1/filmes', methods=['GET'])
def filmes():
    html_doc = urlopen("http://www.rioanil.com.br/cinema").read()
    soup = BeautifulSoup(html_doc, "html.parser")

    data = []
    
    for dataBox in soup.find_all("div", class_="col-xs-12 col-sm-6 col-md-6 col"):
        thumbObj = dataBox.find("div", class_="thumb")
        nomeObj  = dataBox.find("div", class_="descricao").find("a", class_="aspNetDisabled link-default")
        exibicao = dataBox.find("div", class_="titulo-exibicao")
        sala     = dataBox.find("div", class_="titulo-sala").find("b")
        horario  = dataBox.find("div", class_="titulo-hora").find("span")
        #classificacao = dataBox.find("p", class_="classicacao").find("span")
        data.append({
            'nome':nomeObj.text.strip(),
            'thumb':thumbObj.input['src'].strip(),
            'exibicao':exibicao.text.strip(),
            'sala':sala.text.strip(),
            'horario': horario.text.strip(),
            #'classificacao':classificacao.text.strip()
        })

    return jsonify({ 'filmes': data})

if __name__ == '__main__':
    app.run(debug=True)
   # port = int(os.environ.get('PORT', 5000))
    #app.run(host='127.0.0.1', port=port)