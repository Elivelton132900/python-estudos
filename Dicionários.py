"""
Dicionários
Dicionários são coleções do tipo chave/valor
Dicionários são representados por chaves {}

forma 1
países = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
forma 2
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')

Chave e valor são separados por dois pontos 'chave:valor'
Tanto chave quanto valor podem ser de qualquer tipo de dado
Podemos misturar tipos de dados
"""

"""
Acessando valor via chave:
print(paises['br'])
Acessando via get - Forma recomendada, porque caso não encontre a chave, retorna o valor None e não dá erro como no via chave apenas.
print(paises.get['br'])

Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada
pais = paises.get('py', 'Não encontrado')

Tuplas em dicionários: Bom de usar porque são imutáveis
localidades = {
    (35.6895, 39.6917): 'Escritório em Tóquio'
    (40.7128, 74.0060): 'Escritório em Nova York'
    (37.7749, 122.4194): 'Escritório em São Paulo'
}

Adicionando valor :
receita = {'jan': 100, 'fev': 120, 'mar': 300}
receita['abr'] = 350
ou
novo_dado = {'mai': 500}
receita.update(novo_dado) #receita.update({'mai': 500})

Atualizando dados:
receita['mai'] = 550
ou
receita.update({'mai': 600})
Dicionário não aceita chaves repetidas

Remover dados:
receita.pop('mar')
Ao removermos um objeto, o valor deste objeto é sempre retornado.
ou
del receita['fev']
O valor removido não é retornado
"""

"""
Métodos:
d = {'a': 1, 'b': 2, 'c': 3}

d.clear() = Limpa o dicionário
-----------------------
novo = d.copy() --- Deep copy: Uma atualização de uma coleção não afeta a outra
print(novo)
novo = ['d'] = 4
print(d)
print(novo)
-----------------------
novo = d - Shallow copy: Uma atualização de uma coleção afeta a outra
print(novo)
novo = ['d'] = 4
print(d)
print(novo)

outro = {}.fromkeys('a', 'b') -- a: chave   b: valor
usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido') = cada informaçãp dentro dos colchetes vira uma chave e 'desconhecido' o valor dessas chaves.
veja = {}.fromkeys('teste', 'valor') --- para cada letra "t, e, s, t, e" é atribuido o valor 'valor'; e as letras viram chaves.; porem as ultimas letras 't, e' não viram chaves por serem repetidas.

"""

outro = {}.fromkeys('a', 'b')
print(outro)