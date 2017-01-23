import postgresql

def setconnfig():
    db = postgresql.open('pq://developer:colleto@localhost:5432/tcguaruja_test')
    return db