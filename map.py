"""
Map

Faz mapeamento de valor para função.
Map recebe dois parâmetros: 1: A função 2: Um iterável
Retorna um map Object


"""

"""
import math


def area(r):
    # Retorna a área de um circulo com raio 'r'
    return math.pi * (r ** 2)


raios = [2, 5, 10, 20, 35, 12, 32, 15, 23]

areas = []
for r in raios:
    areas.append((area(r)))
print(areas)

# FORMA MAP
areas = map(area, raios)

print(areas)
print(list(areas)) # Pode-se converter para qualquer coleção


# FORMA MAP COM LAMBDA
print(list(map(lambda r: math.pi * (r ** 2), raios)))
# Após utilizar a função map() depois da primeira utilização do resultado ele zera

"""

cidades = [('berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28),
           ('Londes', 22)]

print(cidades)

# Farenheit = 9/5 * c + 32

c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)

print(list(map(c_para_f, cidades)))

# Parâmetros Map: (função, iterável)
