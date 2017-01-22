from database import db_session

class HandleCategoria(object):
    def add(self, newcategoria):
        try:
            db_session.add(newcategoria)
            db_session.commit()
        except(ValueError):
            pass
        finally:
            return 'Cadastro efetuado com sucesso'

    def list(self):
        try:
            categorias = db_session.query.all()
            return categorias
        except(ValueError):
            pass