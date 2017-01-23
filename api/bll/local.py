import falcon

class localBLL(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = ('\nNão somos ricos pelo que temos, e sim pelo que não precisamos ter.\n\n'
                     '    ~ Immanuel Kant\n\n')

    def on_post(self, req, resp):
        pass

    def on_put(self, req, resp):
        pass

    def on_delete(self, req, resp):
        pass