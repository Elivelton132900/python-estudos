"""
Conhecendo o Pickle

A função do Pickle é realizar o seguinte processo:

Objeto Python - Binarização
Binarização - Objeto Python

O módulo Pickle não é seguro contra dados maliciosos e desta forma
não é recomendado trabalhar com arquivos pickle vindos de outras pessoas
--------------------------------------------------
felix = Gato('Felix')
pluto = Cachorro('Pluto')


# Escrita
with open('animais.pickle', 'wb') as arquivo:
    pickle.dump((felix, pluto), arquivo)
---------------------------------------------------

"""


import pickle


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f'{self.__nome} está comendo...')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self.nome} está miando...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self.nome} está latindo...')


with open('animais.pickle', 'rb') as arquivo:
    gato, cachorro = pickle.load(arquivo)
    print(f'O gato chama-se {gato.nome}')
    gato.mia()
    print(f'O tipo do gato é {type(gato)}')
    print(f'O cachorro chama-se {cachorro.nome}')
    cachorro.late()
    print(f'O tipo do cachorro é {type(cachorro)}')
