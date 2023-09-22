"""
Funções com Parâmetro Padrão

- Passagem de parâmetro seja opcional


# Função que exponencia um número de acordo com o número e a potência desejada
# Se a potência não for informada, o '=2' coloca por padrão que seja 2


def exponencial(numero, potencia=2):
    return numero ** potencia


# Em funções Python, os parâmetros com valroes default devem sempre estar ao final da declaração

#ERRO
def teste(num=2, potencia):
    return num ** potencia


# Variável global
instrutor = 'Geek'

def diz():
    instrutor = 'Python'
    return 'oi',instrutor
#Variáveis locais prevalecem sobre variáveis globais (imprime oi, python)
-----------------------------------------------------------------------------
total = 0

def incrementa():
    global total
    total += 1
    return total

# 'global' informa que a função usará uma variável fora do escopo da função

"""


# Funções que são declaradas dentro de funções, e funções dentro de funçaõ

def fora():
    contador = 0

    def dentro():
        nonlocal contador

        contador = contador + 1
        return contador
    return dentro()

print(fora())

# nonlocal informa que usará uma variável da função acima