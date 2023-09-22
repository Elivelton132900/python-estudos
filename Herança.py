"""
POO - Herança

A idéia de herança é de reaproveitar código e extensão de classes

Com a herança, apartir de uma classe existente, nós extendemos outra classe
que passa a herdar atributos e métodos da classe herdada

Existe alguma entidade genérica o suficiente para encapsular os atributos e métodos comuns
a outras entidades?

class Cliente:

    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Funcionario:

    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


cliente1 = Cliente('Lana', 'Del Rey', '123.456.789-00', 3000)
funcionario1 = Funcionario('Billie', 'Eilish', '123.456.789-11', 1234)
------------------------------------------------------------------------

Quando uma classe herda de outra classe ele herda TODOS os atributos e métodos da classe herdada
Quando uma classe herda de outra classe a classe herdada é conhecida por:
          [Pessoa]
          - Super Classe
          - Classe Pai
          - Clase Base
          - Classe Genérica

Quando uma clase herdada e outra classe, ela é chamada:
          [Cliente, Funcionário]
          - Sub Classe
          - Classe Filha
          - Classe Específica

class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    # Cliente herda de Pessoa

    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf)  # Forma não comum de acessar dados da super classe
        self.__renda = renda


class Funcionario(Pessoa):
    # Funcionário de pessoa

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)  # Forma comum de acessar dados da super classe
        self.__matricula = matricula


cliente1 = Cliente('Lana', 'Del Rey', '123.456.789-00', 3000)
funcionario1 = Funcionario('Billie', 'Eilish', '123.456.789-11', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

print(cliente1.__dict__)
print(funcionario1.__dict__)
-----------------------------------------------------------------
# Sobrescrita de Métodos (Overriding)
Sobrescrita de método ocorre quando reescrevemos/reimplementamos um método presente na super classe
em classes filhas
"""


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    # Cliente herda de Pessoa

    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf)  # Forma não comum de acessar dados da super classe
        self.__renda = renda


class Funcionario(Pessoa):
    # Funcionário de pessoa

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)  # Forma comum de acessar dados da super classe
        self.__matricula = matricula

    def nome_completo(self):
        print(super().nome_completo())
        print(self._Pessoa__cpf)
        return f'Funcionário: {self.__matricula} Nome: {self._Pessoa__nome}'


cliente1 = Cliente('Lana', 'Del Rey', '123.456.789-00', 3000)
funcionario1 = Funcionario('Billie', 'Eilish', '123.456.789-11', 1234)

print(cliente1.nome_completo())
print('')
print(funcionario1.nome_completo())