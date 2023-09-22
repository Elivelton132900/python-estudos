"""
POO- Herança Múltipla

Herança Múlyipla nada mais é do que a possibilidade de uma classe herdar de múltiplas classes,
fazendo com que a classe filha herde todos os atributos e métodos de todas as classes herdadas

A herança múltiplica pode ser feita de duas maneiras:
          -Por Multiderivação Direta;
          -Por Multiderivação Indireta

class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class MultiDerivada(Base1, Base2, Base3):
    pass


# Exemplo de Multiderivação Indireta

class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


class Multiderivada(Base3):
    pass

-----------------------------------------------------------
Não importa se a derivação é direta ou indireta. A classe que realizar a herança
herdará todos os atributos e métodos das super classes
"""


# Multideviração Direta


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def comprimentar(self):
        return f'Eu sou {self.__nome}'


class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar!'


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra!'


class Pinguim(Terrestre, Aquatico):

    def __init__(self, nome):
        super().__init__(nome)


baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())
print("")

tatu = Terrestre('Xim')
print(tatu.andar())
print(tatu.cumprimentar())
print("")

tux = Pinguim('Tux')
print(tux.andar())
print(tux.nadar())
print(tux.cumprimentar())  # Eu sou Tux da terra! Method Resolution Order

# Objeto é instância de...?

print(f'Tux é instância de Pinguim? {isinstance(tux, Pinguim)}')  # True
print(f'Tux é instância de Aquático? {isinstance(tux, Aquatico)}')  # True
print(f'Tux é instância de Terrestre? {isinstance(tux, Terrestre)}')  # True
print(f'Tux é instância de Animal? {isinstance(tux, Animal)}')  # True

print(f'Tux é instância de object? {isinstance(tux, object)}') # True
# Toda classe herda de object 