"""
Listas Aninhadas (listas dentro de listas)

listas = [[1,  2, 3], [4, 5, 6], [7, 8, 9]]

for lista in listas:
    for num in lista:
        print(num)

[[print(valor) for valor in lista] for lista in listas]
-----------------------------------
def cria_matriz(num1, num2):
    tabuleiro = [[numero for numero in range(1, num1+1)]for valor in range(1, num2+1)]
    return tabuleiro


print(cria_matriz(2, 6))
------------------------------------
"""


