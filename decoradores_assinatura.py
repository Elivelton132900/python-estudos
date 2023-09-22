"""
Decorators com diferentes assinaturas

def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou a/o {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor.'


print(saudacao('Angelina'))

print(ordenar('Picanha', 'Batata Frita'))  # TypeError: aumentar() takes 1 positional argument but 2 were given
# para resolver, utilizamos um padrão de projeto chamado Decorator Pattern
-----------------------------------------------------------

A assinatura de uma função é representada pelo seu retorno, nome e paâmetros de entrada.
-----------------------------------------------------------
# Revolvendo com o Decorator Pattern

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, meu nome é {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal} acompanhado de {acompanhamento}, por favor.'


print(saudacao('Angelina'))
print(ordenar('Picanha', 'Batata Frita'))


@gritar
def lol():
    return 'lol'


print(lol())
-------------------------------------------------------

"""


# Decorator com argumentos

def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)


@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2


print(soma_dez(10, 12))
print(soma_dez(1, 21))  # Valor incorreto

print(comida_favorita('pizza', 'churrasco'))
print(comida_favorita('sanduiche', 'churrasco'))