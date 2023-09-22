"""
Introdução ao módulo Unittest

Unittest -> Testes Unitários
É a forma de se testar unidades individuais de código fonte
Unidade Individual pode ser: Funções, métodos, classes, módulos e etc

Para criar nossos testes, criamos classes que herdam de unittest.TestCase
e a partir de então ganhamos todos os assertions presentes no módulo

para rodar os testes, utilizamos unittest.main()

Method	             Checks that
assertEqual(a, b)	  a == b
assertNotEqual(a, b)  a != b
assertTrue(x)	      bool(x) is True
assertFalse(x)	      bool(x) is False
assertIs(a, b)	      a is b
assertIsNot(a, b)	  a is not b
assertIsNone(x)	      x is None
assertIsNotNone(x)	  x is not None
assertIn(a, b)	      a in b
assertNotIn(a, b)	  a not in b

Por convenção todos os testes em um test case, devem ter seu nome iniciado
test_

Para executar os testes com unittest
python nome_do_modulo.py

Para executar os  testes com unittest no modo verbose
python nome_do_modulo.py -v

Podemos utilizar (e é recomendado) utilizar docstrings
"""

"""
arquivos dessa aula:
atividades.py
testes.py
"""
# Utilizando TDD