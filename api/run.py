import falcon
from bll.categoria import categoriaBLL
from bll.usuario import usuarioBLL
from bll.local import localBLL
from bll.votacao import votacaoBLL
from wsgiref import simple_server

# Definição do app
app = falcon.API()

# Handlers
categoria = categoriaBLL()
usuario = usuarioBLL()
local = localBLL()
votacao = votacaoBLL()

# Routers
app.add_route('/categoria', categoria)
app.add_route('/usuario', usuario)
app.add_route('/local', local)
app.add_route('/votacao', votacao)

#app.add_error_handler(ManagerError, ManagerError.handle)


if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.server_forever()