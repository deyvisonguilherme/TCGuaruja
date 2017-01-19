import logging
from flask import Flask, request
from flask_json import FlaskJSON, JsonError, json_response, as_json
from handlers import categorias, locais, usuarios, votacao
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
json = FlaskJSON(app)


@app.route('/', methods=['GET', 'POST'])
def root():
    return json_response(status=200, mensagem='API tcguaruja')

@app.errorhandler(404)
def page_not_found():
    return 'Page not Found'


@app.route('/categoria/v1.0/add', methods=['POST'])
def addcategoria():
    negocio = categorias
    return negocio


@app.route('/categoria/v1.0/getlist', methods=['GET'])
def getcategorias():
    negocio = categorias
    return negocio


@app.route('/categoria/v1.0/get', methods=['GET'])
def getcategoria():
    negocio = categorias
    return negocio

@app.route('/categoria/v1.0/del', methods=['POST'])
def delcategoria():
    negocio = categorias
    return negocio

if __name__ == '__main__':
    formatter = logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
    managerror = RotatingFileHandler('logerrors.log', maxBytes=10000000, backupCount=5)
    managerror.setLevel(logging.INFO)
    app.logger.addHandler(managerror)
    app.run(host='127.0.0.1', port=5000, debug=True)
