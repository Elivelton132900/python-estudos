"""
Any e All

all() - Retorna True se todos elementos do iterável são verdadeiros ou se o iterável está vazio
print(all([0, 1, 2, 3, 5]))  # False, = 0 True
print(all([1, 2, 3, 5]))     # True
print(all([]))               # True

nomes = ['Carlos', 'Cristina', 'Cassiano', 'Daniel']
print(all([nome[0]] == 'C' for nome in nomes))     # False, 'Daniel' começa com 'D'

Any() - Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False
print(any([0, 1, 2, 3, 4]))           #True, apenas o 0 False
print(any([0, False, {}, (), []]))    #False, todos False.
"""


