import falcon
from api.dal.categoria import categoriaDAL

class categoriaBLL(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = ('\nO homem não é nada além daquilo que a educação faz dele.\n\n'
                     '    ~ Immanuel Kant\n\n')

    def on_post(self, req, resp):
        try:
            negocio = categoriaDAL()
            negocio.add(req['categoria'])
            resp.status = falcon.HTTP_200
            resp.body = ('cadastro efetuado com sucesso')
        except(ValueError):
            pass


    def on_put(self, req, resp):
        pass

    def on_delete(self, req, resp):
        pass