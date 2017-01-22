import unittest
from models import ModelCategoria
from handlers.categorias import HandleCategoria


class TestCategoria(unittest.TestCase):
    def testaddcategoria(self):
        # sempre que executar a gravação mudar o valor de entrada, pôs banco esta com chave unique para
        # o campo nm_categoria
        c = ModelCategoria('test3')
        control = HandleCategoria()
        negocio = control.add(c)
        self.assertEqual('Cadastro efetuado com sucesso', negocio)


if __name__ == '__main__':
    unittest.main()
