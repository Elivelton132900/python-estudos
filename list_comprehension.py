"""
List Comprehension

-Utilizando List Comprehensions nós podemos gerar novas listas com dados processador a partir
de outro iterável.

# Síntaxe:

[ dado for dado in iterável ]
-----------------------------------
numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)
-----------------------------------
nome = 'Geek University'

print([letra.upper() for letra in nome])
-------------------------------------
def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome

amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']
print([caixa_alta(amigo) for amigo in amigos])
---------------------------------------
"""


# Estruturas condicionais lógicas em List Comprehension

numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]
print(pares, impares)

# Refatorado
# O módulo de números pares por 2 é 0, e 0 == False; Not False == True
pares = [numero for numero in numeros if not numero % 2]

# O módulo de número ímpares por dois é 1, e 1 == True
impares = [numero for numero in numeros if numero % 2]
print(pares, impares)


lista = [1, 2, 'oi']
linha = [dado for dado in lista if type(dado) == str]


print(linha)
print(linha)