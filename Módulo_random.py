"""
Módulo Random

Módulos são outros arquivos em Python

Módulo Random - Possui várias funções para geração de números pseudo-aleatório.

# Modo um: importando todo módulo
import random
# Ao realizar import de todo o módulo, todas as funções, atributos, classes e propriedades que tiverem
# Dentro do módulo ficarão disponívels (ficarão em memória), por isso, não é recomendado


# random() - Retorna um número aleátorio entre 0 e 1
print(random.random())
# Para utilizar a função random(), colocamos o nome do pacote e o nome da função separador por um ponto.
----------------------

# Forma 2: Importando uma função específica do módulo para não importar toda a biblioteca
from random import random

for i in range(10):
    print(random())
----------------------
# Uniform() - Gera um número pseudo-aleatório real entre os valores estabelecidos

from random import uniform

count = 0
for i in range(99):
    print(uniform(1, 10))
-------------------------
from random import randint

# randint() - gera valores pseudo-aleatórios inteiros entre os números estabelecidos

for i in range(6):
    print(randint(1, 61), end=', ')
------------------------
# choice() - Mostra um valor aleatório entre um iterável
from random import choice


jogadas = ['Pedra', 'Papel', 'Tesoura']
print(choice(jogadas))
------------------------


"""


from random import randint

for i in range(6):
    print(randint(1, 18), end=', ')

