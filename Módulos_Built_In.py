"""
Módulos integrados

# Utilizando alias(apelidos) para módulos/funções
import random as rdm
print(rdm.random())
---------------------------

# Podemos importar todas as funções de um módulo utilizando o *

from random import *
print(random())
---------------------------
from random import randint as rdi, random as rdm

print(rdi(1, 10))
print(rdm())
---------------------------


"""


from random import (
    random,
    randint,
    shuffle,
    choice
)


