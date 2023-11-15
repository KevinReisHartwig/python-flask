from app import app
from flask import render_template

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/menu.html')
def menu():
    return render_template('menu.html')

@app.route('/listadespesaspagas.html')
def listadespesaspagas():
    return render_template('listadespesaspagas.html')

@app.route('/listadeobras.html')
def listadeobras():
    return render_template('/listadeobras.html')

@app.route('/listaContratos.html')
def listaContratos():
    return render_template('listaContratos.html')

@app.route('/cadastrarobra.html')
def cadastrarobra():
    return render_template('cadastrarobra.html')

@app.route('/cadastrardespesapaga.html')
def cadastrardespesapaga():
    return render_template('cadastrardespesapaga.html')

@app.route('/cadastrarcontrato.html')
def cadastrarcontrato():
    return render_template('cadastrarcontrato.html')

@app.route('/sitemap.html')
def sitemap():
    return render_template('sitemap.html')
