"""
Reduce

A partir do Python 3+ reduce() não é mais uma função built-in;
é necessário importá-lo do módulo 'functools'

Guido Van Rossum: Utilizar apenas se necessário, loop for é mais legível.

A função Reduce recebe dois parametros: (função, iterável)

def funcao(x, y):
    return x * y

A função reduce() trabalha das seguintes formas:
    passo 1: res = f(a1, a2)    # Aplica a função nos dois primeros elementos da coleção e guarda o resultado
    passo 2: res2 = f(res1, a3) # Aplica a função passando o resultado do passo1 mais o terceiro elemento e guarda o res
    Isso se repete até o final
    passo 3: res3 = f(res2, a4)

reduce() pode ser interpretado:


funcao(funcao(funcao(a1, a2), a3), a4)

"""


from functools import reduce

dados = [2, 3, 4, 5]

multi = lambda x, y: x*y
res = reduce(multi, dados)

print(res)  # 2 * 6 = 6 | 6 * 4 = 24 | 24 * 5

# Um loop

res = 1

for n in dados:
    res = res * n

print(res)