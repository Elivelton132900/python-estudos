"""
Generator Expression

Tuple Comprehension == Generators

Após a utilização é apagado da memória assim como Map e Filter
Generator é mais perfomático do que outros comprehensions e exige menos processamento da máquina

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

res  = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)
print(tuple(res))

-----------------------------------

"""

"""
from sys import getsizeof
# Getsizeof Retorna a quantidade de bytes em memória do elemento passado como memória

# Lista de números com List Comprehension

list_comp = getsizeof([x * 10 for x in range(1000)])
set_comp = getsizeof({x * 10 for x in range(1000)})
dict_comp = getsizeof({x: x * 10 for x in range(1000)})
generator = getsizeof(x * 10 for x in range(1000))

print(f'List comprehension: {list_comp} bytes')
print(f'set comprehension {set_comp} bytes')
print(f'dict comprehension {dict_comp} bytes')
print(f'Generator Expression {generator} bytes')
"""

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(tuple(nome[0] == 'C' for nome in nomes))