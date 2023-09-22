"""
Funções com retorno

Quando não retorna nenhum valor, retorna None

def quadrado_de_7():
    print(7*7)
ret = quadrado_de_7()

print(f"Retorno {ret}")           - Retorna None
-------------------------------------------------------
def quadrado_de_7():
    return 7*7
ret = quadrado_de_7()

print(f"Retorno {ret}")          - Retorna o quadrado de 7

deve-se usar a palavra reservada return para retornar algum valor, e não é necessário criar uma
variável uma variável para receber a função, e pode-se usá-la em outras funções

OBS: Return
Return finaliza a função, sai da execução da função
Podemos ter, em uma função, diferentes returns
Podemos em uma função retornar qualquer tipo de dado e até mesmo multiplos valores

"""


from random import random

def joga_moeda():
    if random() > 0.5:
        return 'Coroa'
    return 'Cara'

print(joga_moeda())
