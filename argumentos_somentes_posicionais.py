"""
Argumentos somente posicionais
Isso significa que não podemos fazer, por exemplo (
valor = '67.3'
print(float(valor))
Isso significa que não podemos fazer, por exemplo print(float(x=valor))

/ = Não precisa fazer 'argumento='algo'. Tudo antes do '/' não precisa ser informado como nomeamento
* = precisa fazer 'argumento'=algo. Tudo depois do '*' precisa ser nomeado como 'argumento='algo'
"""


def cumprimenta_v1(nome):
    return f'Olá {nome}'


# print(cumprimenta_v1(nome='Olá')) # Funciona normalmente


def cumprimenta_v2(nome, /):
    return f'Olá {nome}'


# print(cumprimenta_v2(nome = 'Lana'))
# TypeError: cumprimenta_v2() got some positional-only arguments passed as keyword arguments: 'nome'


def cumprimenta_v3(nome, /, mensagem='Olá'):
    return f'{mensagem} {nome}'


# print(cumprimenta_v3('Lana'))
# print(cumprimenta_v3('Lana', mensagem='Hello'))
# print(cumprimenta_v3('Lana', 'bem-vinda'))


def cumprimenta_v4(nome, mensagem='Olá', /):
    return f'{mensagem} {nome}'


print(cumprimenta_v4('Lana'))
print(cumprimenta_v4('Lana', 'bem-vinda'))
# print(cumprimenta_v4('Lana', mensagem='Hello')) TypeError: cumprimenta_v4() got some positional-only arguments passed
# as keyword arguments: 'mensagem'


def cumprimenta_v5(*, nome):  # Indica que todos os argumentos depois do * devem ser informados
    return f'Olá {nome}'


print(cumprimenta_v5(nome='Lana'))
# print(cumprimenta_v5('Lana'))   TypeError: cumprimenta_v5() takes 0 positional arguments but 1 was given


def cumprimentar_v6(nome, /, mensagem1='Olá', *, mensagem2):
    return f'{mensagem1} {nome} {mensagem2}'


print(cumprimentar_v6('Lana', mensagem1='Hello', mensagem2='Tenha um bom dia'))
print(cumprimentar_v6('Lana', mensagem2='tenha um bom dia'))
# print(cumprimentar_v6('Lana', 'Oi', 'Vamos?')) TypeError: cumprimentar_v6() takes from 1 to 2 positional arguments but
# 3 were given


