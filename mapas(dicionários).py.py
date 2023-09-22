"""
Mapas = Conhecidos em Python vcomo dicionários

receita = {'jan': 100. 'fev':250, 'mar':400}
for chave in receita: Imprime as chaves
    print(chave)

for chave in receita: Imprime o valor das chaves
    print(receita[chave])
ou
print(receita.keys()) = para imprimir as chaves
print(receita.values()) = para imprimir os valores

for chave in receita.keys(): Imprime as chaves
    print(chave)

for chave in receita.values(): Imprime o valor das chaves
    print(valor)

print(receita.items()) = gera uma lista contendo tuplas contendo chave:valor
for chave, valor in receita.items():
    print(f"Chave = {chave} valor = {valor}")
"""

"""
sum(receita.values()) = Retorna a soma dos valores do dicionário
max(receita.values()) = Retorna o valor máximo do dicionário 
min(receita.values()) = Retorna o valor mínimo do dicionário
len(receita) = Retorna o tamanho do dicionário
"""