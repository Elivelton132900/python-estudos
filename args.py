"""
*args

- O *argdss é um parâmetro, como outro qualquer. Isso significa que você poderá
chamá-lo de qualquer coisa, desde que comece com asterísco.

Exemplo:
*xis

Mas, por convenção, utilizamos o *args para definí-lo.

O parâmetro *args utilizado em uma função, coloca os valores extras informados como
entrada em uma tupla.
def soma(num1=1, num2=2, num3=3):
    return num1 + num2 + num3

print(soma())
# Parâmetros limitados a três, e caso fosse adicionar algum número a mais, teria que
# adiciomar um parâmetro a mais e adicioná-lo no return

#SOLUÇÃO

def soma(*args):
    return sum(args)

print(soma(1, 2, 3, 4, 5, 6))

# Pode-se adicionar quantos parâmetros que quiser.
# Args não é obrigatório


#def soma(*args):
#    return sum(args)


# Caso o argumento passado para a função soma seja uma coleção, ele não fará a operação
# Porque será uma lista dentro de uma tupla, por exemplo.

#SOLUÇÃO:

a = [1, 2, 3, 4, 5, 6, 7]

def soma(*args):
    return sum(args)

print(soma(*a))

# O '*' Informa que é uma coleção e o Python deverá desempacotá-lo.

"""

