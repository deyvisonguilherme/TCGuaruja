import postgresql

class Config(object):
    def configurationDatabase(self):
        try:
            db = postgresql.open('pq://developer:colleto@localhost:5432/tcguaruja')
            db.connect()
            return db
        except(ValueError):
            pass