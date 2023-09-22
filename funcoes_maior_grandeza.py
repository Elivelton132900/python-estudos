"""
Funções da Maior Grandeza - Higher Order Functions - HOF

Quando uma linguagem de programação suporta HOF, indica que podemos ter funções
que retornam outras funções como resultado ou mesmo que podemos passar funções
como argumentos para outras funções, e até mesmo criar variáveis do tipo funções
nos nossos programas

Em Python, as funções são Cidadões de Primeira Classe (First Class Citizen)

def somar(a, b):
    return  a + b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


print(calcular(4, 3, somar))
print(calcular(4, 3, diminuir))
print(calcular(4, 3, multiplicar))
print(calcular(4, 3, dividir))
---------------------------------------------------
# Nested Functions - Funções Aninhadas


# Em Python, podemos também ter funções dentro de funções, que são conhecidas por Nested Functions
# Ou também Inner Functions (Funções Internas)


from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Suma Daqui ', 'Gosto muito de você '))
    return humor() + pessoa

print(cumprimento('Angelina'))
print(cumprimento('Lana'))
----------------------------------------------------
# Retornando funções de outras funções

from random import choice

def faz_me_rir():
    def rir():
        return choice(('hahahahaha', 'kkkkkkkkkk', 'yayayayayay'))
    return rir


rindo = faz_me_rir()
print(rindo())
--------------------------------------------------------
"""


# Inner Functions (Funções Internas / Nested Functions) podem acessar o escopo de funções mais externas

from random import choice


def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahahahaha', 'lololololololo', 'kkkkkkkkkkkkk'))
        return f'{risada} {pessoa}'
    return dando_risada


rindo = faz_me_rir_novamente('Lana')

print(rindo())
print(rindo())
print(rindo())