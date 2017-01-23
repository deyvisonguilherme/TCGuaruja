import falcon

class votacaoBLL(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = ('\nA amizade é semelhante a um bom café; uma vez frio, não se aquece sem perder bastante do primeiro sabor.\n\n'
                     '    ~ Immanuel Kant\n\n')

    def on_post(self, req, resp):
        pass

    def on_put(self, req, resp):
        pass

    def on_delete(self, req, resp):
        pass