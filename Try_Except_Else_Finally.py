"""
Try / Except / Else / Finally

Toda entrada deve ser tratada
A função do usuário é DESTRUIR seu sistema.

try:
    num = int(input('Informe um número '))
except ValueError:
    print('Valor incorreto')
else:               # Else somente é executado se não houver um erro
    print(f'Você digitou o número {num}')
------------------------------------

try:
    num = int(input('Informe um número '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou o número {num}')
finally:
    print('Executando o finally')

# O bloco finally é sempre executado independente se houve excessão ou não
# Finally geralmente é utilizado para fechar ou desalocar recursos
------------------------------------

# EXEMPLO ERRADO ------------

def dividir(a, b):
    return a/b


num1 = int(input('Informe o primeiro número '))

try:
    num2 = int(input('Informe o segundo número '))
except ValueError:
    print('O valor precisa ser inteiro e numérico')

try:
    print(dividir(num1, num2))
except NameError:
    print('Valor incorreto')
------------------------------------
"""

"""
def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possível realizar uma divisão por zero'

num1 = input('Informe o primeiro número ')
num2 = input('Informe o segundo número ')

print(dividir(num1, num2))
"""


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Valor incorreto: {err}'


num1 = input('Informe o primeiro número ')
num2 = input('Informe o segundo número ')

print(dividir(num1, num2))

