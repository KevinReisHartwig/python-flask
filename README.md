# python-flask

Roteiro para instalar o python e o flask, e como usar no seu site. 

Azul = comandos do powerShell
Amarelo = comandos do terminal VS CODE
Verde = linha de código 

Etapa 1 – fazer o download do python, depois abrir a variáveis de ambiente ir em path pegar o iniciar em em propriedades do python clicar em editar o path e depois em novo e colar o “iniciar em” e depois mais um novo com o mesmo “iniciar em” copiado mas com” /Scripts” no final e depois abrir o power shell como administrador digitar “ Set-ExecutionPolicy Unrestricted ” depois enter e depois S enter, abrir o VS code e depois o terminal dele para criar o ambiente virtual usando o comando “ python -m venv venv ” e depois o “.\venv\Scripts\Activate” para ativar o servidor e depois instalar o flash usando “pip install flask”.
Etapa 2 – Iniciar o ambiente virtual usando o “ .\venv\Scripts\Activate ” se ainda não estiver, criar uma pasta chamada app e dentro dela um arquivo chamado “__init__.py” dentro desse arquivo escrever:

from flask import Flask
app = Flask(__name__)
from app import routes
depois criar um arquivo chamado routes.py colocar o código: 

from app import app
from flask import render_template

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')
@app.route('/menu.html')
def menu():
    return render_template('menu.html')

para cada pagina html que deseja adicionar usar o mesmo esquema como por exemplo esse:
@app.route('/menu.html')
def menu():
    return render_template('menu.html')

usar o pip install python-dotenv no terminal para criar variáveis de ambiente
criar a pasta.flaskenv e dentro dela colocar:

FLASK_APP=template.py
FLASK_ENV=development

Flask run para testar no terminal.
Etapa 3 – para diminuir repetição de código você pode criar um arquivo chamado base.html por exemplo e colocar o código que se repete em todos os html como por exemplo esse aqui que tem em todas as páginas html:

"<!doctype html>
<html lang="pt-br" data-bs-theme="auto">
aa<head><script src="/assets/js/color-modes.js"></script>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
    <meta name="generator" content="Hugo 0.118.2">
    <link rel="icon" href="./menu/img/OIP.jpeg" type="image/png">
    <script src="/assets/dist/js/bootstrap.bundle.min.js"></script>
    {% block conteudo %}
    {% endblock %}
</body>
</html>"
  
depois é só colocar esses códigos no início da página {% extends 'base.html' %}
    {% block conteudo %}
E no final da página colocar:
    {% endblock %}

Etapa 4 – Para colocar as imagens e o css precisa criar dentro da pasta app a pasta static e devemos colocar as Imagens, CSS e os JS nessa pasta e para mudar os css/js/image é só colocar por exemplo esse código que funciona em todos os 3 casos:
<link rel="icon" href="{{url_for('static', filename='icon.jpeg')}}" type="image/png">

