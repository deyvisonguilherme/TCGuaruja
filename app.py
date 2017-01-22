from flask import Flask
from flask_json import FlaskJSON, json_response
from database import db_session
from handlers.categorias import HandleCategoria
from models import ModelCategoria

app = Flask(__name__)
json = FlaskJSON(app)


@app.route('/', methods=['GET', 'POST'])
def root():
    return json_response(status=200, message='API tcguaruja')

@app.route('/categoria/v1.0/add/<cat>', methods=['GET','POST'])
def addcategoria(cat):
    c = ModelCategoria(cat)
    control = HandleCategoria()
    negocio = control.add(c)
    return json_response(status = 200, message = negocio)


@app.route('/categoria/v1.0/getlist', methods=['GET'])
def getcategorias():
    negocio = ModelCategoria.query.all()
    return negocio

'''
@app.route('/categoria/v1.0/get', methods=['GET'])
def getcategoria():
    negocio = categorias
    return negocio

@app.route('/categoria/v1.0/del', methods=['POST'])
def delcategoria():
    negocio = categorias
    return negocio
'''
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
