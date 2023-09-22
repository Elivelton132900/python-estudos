"""
Sorted

sorted() funciona com qualquer iterável, diferente do sort() que apenas funciona com listas.
sorted() sempre retorna uma lista com os elementos do iterável ordenados

numeros = [2, 3, 1, 4, 6]
print(numeros)

print(sorted(numeros))
print(numeros)   # Sorted não efetua a mudança na lista como sort()
---------------------------------------

numeros = [2, 3, 1, 4, 6]
print(sorted(numeros, reverse=True))  # Ordena do maior para o menor
---------------------------------------

usuarios = [
    {'username': 'Samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username': 'Carla', 'tweets': ['Eu adoro meu gato']},
    {'username': 'Jeff', 'tweets': [], "cor": 'Amarelo'},
    {'username': 'bob123', 'tweets': [], 'cor': 'preto', 'musica': 'Rock'},
    {'username': 'Doggo', 'tweets': ['Eu gosto do meu cachorro', 'Vou sair hoje']},
    {'username': 'Gal', 'tweets': []},
]

print(usuarios)

# Ordenando pelo username, ordem alfabética
print(sorted(usuarios, key=lambda usuario: usuario['tweets']))

# Ordenando pelo número de tweets, menor para o maior
print(sorted(usuarios, key=lambda usuario: len(usuario['tweets'])))

# Ordenando pelo número de tweets, maior para o menor
print(sorted(usuarios, key=lambda usuario: len(usuario['tweets']), reverse=True))
-----------------------------------------


"""


musicas = [
    {'titulo': 'Andromeda', 'tocou': 524},
    {'titulo': 'California', 'tocou': 473},
    {'titulo': 'Cinnamon Girl', 'tocou': 481},
    {'titulo': 'Fuck It I Love You', 'tocou': 509},
    {'titulo': 'Nobody', 'tocou': 451},
]


# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))

# Ordena da mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))
