"""
Listas
-Enquanto houver memória poderá ser criado algum valor naquela lista
-Qualquer tipo de dado: não possuem tipo de dado fixo, então pode-se colocar qualquer tipo de dado
-Colchetes '[]'
"""

#Verificar se está contido:
#if valor in lista: print("Valor encontrado")

"""
lista.sort() = Ordena em ordem crescente
lista.count() = Contar o número de ocorrências de um valor numa lista
lista.append() = Adiciona algum valor na lista (um elemento por vez)
lista.append([]) = Adiciona uma lista dentro de outra lista
lista.extend([]) = Adiciona cada valor como sendo adicional e não dentro de uma lista, e não aceita valor único.
lista.insert(indice, 'novo valor') = Adiciona certo valor no índice mencionado
lista = listaa + listab = Faz uma lista única
lista.extend(listaa) = Mesma coisa do que o de cima
lista.reverse() = Inverte os valores da lista
lista = listaa.copy() = copía uma lista
len(lista) = Fala o tamanho da lista
lista.pop() = Remove o último elmento de uma lista e o retorna
lista.pop(2) = Remove o elemento do índice dado no argumento e o elemento da direita vai para a esquerda
lista.clear() = Remove todos os elementos da lista
lista = lista*3: Repete os elementos da lista 3 vezes
curso = curso.split() = Transforma uma string em lista e separa os elementos da string pelo espaço entre elas
.split(',') = Separa os caracteres com vírgula
curso = ' '. join(lista) = Adiciona espaço entre cada elemento e transforma numa string (no ' ' pode adicionar qualquer caracter para separá-los)

#Enumera o indice e o valor que está contido no índice
cores = ['verde', 'amarelo', 'azul', 'branco']
for indice, cor in enumerate(cores):
    print(indice, cor)

"""
"""
lista.index(6) = retorna o índice onde o argumento está contido, se houver mais de um, retorna o índice do primeiro
lista.index(6, 1) = procura o índice no qual o valor 6 está contido apartir do índice 1
lista.index(6, 7, 10) = Procura o índice do valor 6 entre o índice 7 e 10
"""

"""
Slice:
lista[1::] Inicia no valor do índice dois até o valor do índice final
lista[:2] Começa em 0, e vai do índice 2 - 1
lista[1::2] Começa no índice 1, e vai até o final pulando de 2 em 2
***********Estudar
"""

"""
sum(lista) = Realiza a soma da lista
max(lista) = Retorna o maior valor da lista
min(lista) = Retorna o menor valor da lista
len(lista) = Retorna a quantidade de itens da lista
"""

#lista = [1, 2, 3]
#num1, num2, num3 = lista
#num1 = 1  num2 = 2  num3 = 3

"""
Copiando uma lista para outra (Shallow Copy e Deep Copy)

lista = [1, 2, 3]
print(lista)
nova = lista.copy()
print(nova)
nova.append(4)
print(lista)
print(nova)
#Listas independentes independente se uma sofre modificação ou não. (Deep Copy)
-------------------------------------------------------------------------------
lista = [1, 2, 3]
print(lista)
nova = lista
print(nova)
nova.append(4)
print(lista)
print(nova)
#Utilizamos a cópia via atruibuição e copiamos os dados da lista para a nova lista, mas
#após realizar modificação em uma das listas, essa modificação se refletiu em ambas.
#Isso é chamado de Shallow Copy
"""