import falcon
from bll.categoria import categoriaBLL
from bll.usuario import usuarioBLL
from bll.local import localBLL
from bll.votacao import votacaoBLL

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
