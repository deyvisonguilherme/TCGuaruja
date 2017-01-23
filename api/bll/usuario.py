import falcon

class usuarioBLL(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = ('\nPodemos julgar o coração de um homem pela forma como ele trata os animais.\n\n'
                     '    ~ Immanuel Kant\n\n')

    def on_post(self, req, resp):
        pass

    def on_put(self, req, resp):
        pass

    def on_delete(self, req, resp):
        pass