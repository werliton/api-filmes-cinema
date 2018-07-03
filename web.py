from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import os

app = Flask(__name__)

@app.route('/api/v1/filmes', methods=['GET'])
def filmes():
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

# Lista filmes do Rio Anil
@app.route('/api/v1/cinema/rioanil', methods=['GET'])
def rioanil():
    html_doc = urlopen("http://www.rioanil.com.br/cinema").read()
    soup = BeautifulSoup(html_doc, "html.parser")

    data = []
	   
    for dataBox in soup.find_all("div", class_="col-xs-12 col-sm-6 col-md-6 col"):
        horas = []
        for bxHora in dataBox.find_all("div", class_="titulo-hora"):
            hora = bxHora.find("span")
            horas.append({
				'horario': hora.text.strip()
			})
            
        thumbObj = dataBox.find("div", class_="thumb")
        nomeObj  = dataBox.find("div", class_="descricao").find("a", class_="aspNetDisabled link-default")
        exibicao = dataBox.find("div", class_="titulo-exibicao")
        sala     = dataBox.find("div", class_="titulo-sala").find("b")
        #horario  = dataBox.find("div", class_="titulo-hora").find("span")
		#classificacao = dataBox.find("p", class_="classicacao").find("span")
        data.append({
            'nome':nomeObj.text.strip(),
            'thumb':thumbObj.input['src'].strip(),
            'exibicao':exibicao.text.strip(),
            'sala':sala.text.strip(),
            'horario': horas,
            #'classificacao':classificacao.text.strip()
        })

    return jsonify({ 'filmes': data})


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
    #app.run()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)