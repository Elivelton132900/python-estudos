"""
Named Tuple

São tuplas diferenciadas onde especificamos um nome para a mesma e também parâmetros

"""
from collections import namedtuple
#precisamos definir o nome e parâmetros
#cachoro = namedtuple('cachoro', ['idade', 'raca', 'nome'])
#cachoro = namedtuple('cachorro', 'idade raca nome')

cachorro = namedtuple('cachorro', 'idade, raca, nome')
ray = cachorro(idade = 2, raca = 'Chow-Chow', nome = 'ray')
#print(ray)
#print(ray[0])
#print(ray[1])
#print(ray[2])

print(ray.idade)
print(ray.raca)
print(ray.nome)

