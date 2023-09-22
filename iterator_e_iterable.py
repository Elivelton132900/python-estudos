"""
Iterator e Iterables

Iterator
    - Um objeto que pode ser iterado
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada
nome = 'Geek'  # É um iterable, mas não é um iterator
numeros = [1, 2, 3, 4, 5, 6]  # É um iterable, mas não é um iterator

# print(next(nome))  # TypeError: 'str' object is not an iterator
# print(next(numeros))  # TypeError: 'str' object is not an iterator

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))  # G
print(next(it1))  # e
print(next(it1))  # e
print(next(it1))  # k


Iterable
    - Um objeto que irá retornar um iterator quando a função iter() for chamada


"""



# iteravel (interator) são listas, strings, dicionarios, sets e afins.
# todo iterável tem o método __iter__() transforma num iterável
# para percorrer uma lista num loop for, por exemplo, a lista é transformada num iterador (iterable) para que ele possa
# exibir cada valor
# iterador tem o método __next__()
# para a lista ser um iterador, o python usa o método __iter__, e assim, passa a possuir o método __next__()




lista = [1, 2, 4, 5, 2, 1, '3982']
lista = iter(lista)
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))