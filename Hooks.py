"""
Unittest - antes e após Hooks

Hooks são os testes em si, ou seja, a execução dos testes

setUp() - Executado antes de cada método de teste. Útil para criar instâncias de objetos e outros dados.
tearDown() - É executado ao final de cada método de teste. É útil para excluir dados ou fechar a conexão
com banco de dados.
"""

# Arquivo robo.py

import unittest


class ModuloTest(unittest.TestCase):

    def setUp(self):
        # Configurações do setUp()
        pass

    def test_primeiro(self):
        # setUp vai rodar antes do teste
        # tearDown() vai rodar após o teste
        pass

    def test_segundo(self):
        # setUp vai rodar antes do teste
        # tearDown() vai rodar após o teste
        pass

    def tearDown(self):
        # Configurações do tearDown()
        pass