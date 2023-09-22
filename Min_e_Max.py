"""
Min e Max

max() - Retorna o maior valor em um iterável ou o maior de dois ou mais elementos
print(max(2, 29))

-----------------------------------
min() - Retorna o menor valor em um iterável ou o menor de dois ou mais elementos

nomes = ['Arya', 'Sanson', 'Dora', 'Tim', 'Olivander']
print(max(nomes))  # Retorna o maior elemento (leva em consideração a ordem alfabética)
print(min(nomes))  # Retorna o menor elemento (leva em consideração a ordem alfabética)

print(max(nomes, key=lambda maior: len(maior)))  # Retorna o maior elemento de acordo com o tamanho de caracteres
print(min(nomes, key=lambda maior: len(maior)))  # Retorna o menor elemento de acordo com o tamanho de caracteres
------------------------------------


"""



musicas = [
    {'titulo': 'Andromeda', 'tocou': 524},
    {'titulo': 'California', 'tocou': 473},
    {'titulo': 'Cinnamon Girl', 'tocou': 481},
    {'titulo': 'Fuck It I Love You', 'tocou': 509},
    {'titulo': 'Nobody', 'tocou': 451},
]

print(max(musicas, key=lambda maior: maior['tocou']))
print(min(musicas, key=lambda maior: maior['tocou']))

print(max(musicas, key=lambda maior: maior['tocou'])['titulo'])  # Retorna somente o título
print(min(musicas, key=lambda maior: maior['tocou'])['titulo'])  # Retorna somente o título


# Mesma solução porém com loop for
max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(musica['titulo'])


min = 999999999
for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']

for musica in musicas:
    if musica['tocou'] == min:
        print(musica['titulo'])