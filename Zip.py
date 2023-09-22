"""
Zip

zip() - Cria um iterável (Zip Object) que agrega elemento de cada um dos iteráveis passados como entrada em pares

"""

"""
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [7, 8, 9, 10]
zip1 = zip(lista1, lista2)
print(zip1)
print(type(zip1))

# Pode-se criar uma coleção
# Após o 'desempacotamento' o valor é retirado da memória
print(list(zip1))

zip1 = zip(lista1, lista2, lista3)
print(list(zip1))   # Zip utiliza como parâmetro o menor tamanho em iterável. Isso significa que se estiver trabalhando
# com iteráveis de tamanhos diferentes, irá parar quando os elementos do menor iterável acabar
"""

prova1 = [80, 87, 82]
prova2 = [76, 64, 90]
prova3 = [77, 80, 79]
alunos = ['Pedro', 'Paula', 'Júlia']

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2, prova3)))
print(dict(final))
