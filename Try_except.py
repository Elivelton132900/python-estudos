"""
Try/Except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código. Previnindo
assim que o programa pare de funcionar e o usuário receba mensagens de erro inesperadas

A forma geral mais simples é:
try:
    //execução problemática
except:
    //o que deve ser feito em caso de problema
--------------------------------------------

try:
    geek()
except:
    print('Deu algum problema')
---------------------------------------------

O ideal é sempre tratar de forma específicas os erros e não de forma genérica
try:
    geek()
except NameError:
    print('Você está utilizando uma função inexistente')
---------------------------------------------

try:
    len(5)
except TypeError as err:                     # Permite ver o erro específico que está acontecendo
    print(f'A aplicação gerou o seguinte erro: {err}') # A aplicação gerou o seguinte erro: object of type 'int' has no len()
---------------------------------------------

try:
    lista[0]
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except:
    print('Deu um erro diferente')
"""


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None

dic = {'nome': 'geek'}

print(pega_valor(dic, 'game'))