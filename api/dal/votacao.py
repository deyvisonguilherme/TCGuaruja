from api.dal.configuration import setconnfig

class votacaoDAL(object):
    def add(self):
        conn = setconnfig()
        try:
            insert_categoria = conn.proc('insert_categoria(varchar)')
            ins_cat = insert_categoria('cat')
            ins_cat
        except(ValueError):
            conn.close()
            pass
        finally:
            conn.close()

    def list(self):
        conn = setconnfig()
        try:
            list_categoria = conn.proc('list_categoria()')
            lst_cat = list_categoria()
            lst_cat
        except(ValueError):
            conn.close()
            pass
        finally:
            conn.close()

    def delet(self):
        conn = setconnfig()
        try:
            del_categoria = conn.proc('list_categoria()')
            dl_cat = del_categoria()
            dl_cat
        except(ValueError):
            conn.close()
            pass
        finally:
            conn.close()

    def up(self):
        conn = setconnfig()
        try:
            up_categoria = conn.proc('list_categoria()')
            up_cat = up_categoria()
            up_cat
        except(ValueError):
            conn.close()
            pass
        finally:
            conn.close()