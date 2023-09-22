"""
Dictionary Comprehension

Síntaxe:

{chave:valor for valor in iterável}

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}

print(numeros, quadrado)
---------------------------------------------------------------
numeros = [1, 2, 3, 4, 5, 6]
quadrado = {valor: valor ** 2 for valor in numeros}
print(quadrado)
---------------------------------------------------------------
letras = 'abcde'
numeros = [1, 2, 3, 4, 5]

mistura = {letras[i]: numeros[i] for i in range(len(numeros))}
print(mistura)
--------------------------------------------------------------
"""


numeros = [1, 2, 3, 4, 5]
res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}
print(res)