"""
Filter

Filtra dados de uma determinada coleção

import statistics


# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

#Calculando média dos dados utilizando a função mean()
media = statistics.mean(dados)

# Filter recebe dois parâmetros: (função, iterável)
res = filter(lambda x: x > media, dados)
# Se retorna True é integrado, senão não.
print(list(res))
# Filtra os resultados e imprime e retorna apenas os > que a média
print(list(res))
# Os valores após a execução somem
-------------------------------------------------
paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

#Retorna os países sem os valores em branco
res = filter(None, paises)
#res = filter(lambda pais: len(pais) > 0, paises)

print(list(res))
--------------------------------------------------

usuarios = [
    {'username': 'Samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username': 'Carla', 'tweets': ['Eu adoro meu gato']},
    {'username': 'Jeff', 'tweets': []},
    {'username': 'Doggo', 'tweets': ['Eu gosto do meu cachorro', 'Vou sair hoje']},
    {'username': 'Gal', 'tweets': []},
]
# forma 1
# inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))

# forma 2
inativos = list(filter(lambda u: not u['tweets'], usuarios))
# vazio = False, contendo algum valor = True | Assim filtra os usuários sem nenhum tweet
print(inativos)
------------------------------------------------------

# Criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres

nomes = ['Vanessa', 'Ana', 'Maria']

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)

#Tem mais de 10 letras

palavras = ['sauhsuahsauhsas', 'suahs', 'sauhs', 'sauhsuahsuahsuhsa', 'suahsuahsuahsuahs']

lista = list(map(lambda mais: f'Tem mais de 10 caracteres: {mais}', filter(lambda mais: len(mais) > 10, palavras)))

print(lista)
----------------------------------------------------------
"""



lista = []

while True:
    pergunta = input("[Digite 0 para sair]Digite qualquer palavra ")
    if pergunta == '0':
        break
    else:
        lista.append(pergunta)

print(lista)
lista = list(map(lambda palavras: {palavras}, filter(lambda palavras: len(palavras) < 5, lista)))
print('Palavras com menos de 5 caracteres: ',lista)
