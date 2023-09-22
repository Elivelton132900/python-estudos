"""
**kwargs

Outro parâmetro, mas diferente do *args que coloca os valores extra
em uma tupla, o **kwargs exige que utilizemos parâmetros nomeados, e transforma
esses parâmetros em dicionário.
----------------------------------------
def cumprimento(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza quem você é...'

# Verifica se existe a chave 'geek' in kwargs e se a chave contêm o valor 'Python'
# Verifica se existe a chave geek in kwargs
# Se não existir essa chave, retorna 'Não tenho certeza quem você é...'

print(cumprimento())
print(cumprimento(geek='Python'))
print(cumprimento(geek='Oi'))
print(cumprimento(geek='Especial'))
---------------------------------------
Ordem correta de definição de parâmetros:
 - Parâmetros obrigatório
 - *args
 - Parâmetros default (Não obrigatório)
 - **kwargs

 É necessário manter essa ordem para não haver confusão na distribuição dos argumentos
----------------------------------------
Em dicionários as chaves devem conter os mesmos nomes que os parâmetros.
def soma (a, b, c):
    print(a + b + c)

dic = {'a': 1, 'b': 2, 'c': 3}
soma(**dic)

Caso as chaves de 'dic' fossem diferentes dos parâmetros, o desempacotamento daria erro.

"""


def soma (a, b, c):
    print(a + b + c)

dic = {'a': 1, 'b': 2, 'c': 3}
soma(**dic)