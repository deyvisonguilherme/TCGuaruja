import falcon
from dal.categoria import categoriaDAL

class categoriaBLL(object):
    def on_get(self, req, resp):
        try:
            resp.status = falcon.HTTP_200
            resp.body = ('\nO homem não é nada além daquilo que a educação faz dele.\n\n'
                         '    ~ Immanuel Kant\n\n')
        except(IOError):
            raise falcon.HTTPError(falcon.HTTP_725,'ERROR')

    def on_post(self, req, resp):
        try:
            negocio = categoriaDAL()
            negocio.add(req['categoria'])
            resp.status = falcon.HTTP_200
            resp.body = ('cadastro efetuado com sucesso')
        except(IOError):
            raise falcon.HTTPError


    def on_put(self, req, resp):
        try:
            pass
        except(IOError):
            raise falcon.HTTPError


    def on_delete(self, req, resp):
        try:
            pass
        except(IOError):
            raise falcon.HTTPError