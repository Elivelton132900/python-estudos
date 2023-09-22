"""
POO - Propriedades

Em linguagens de programação como Java, ao declararmos atributos privados nas classes,
costumamos criar métodos públicos para manipulação desses atributos. Esses métodos são conhecidos
por getters e setters, onde os getters retornam o valor do atributo e setters alteram o valor

class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        self.__titular = titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.limite = limite


conta1 = Conta('Lana', 3000, 5000)
conta2 = Conta('Mitski', 2000, 4000)

soma = conta1.get_saldo() + conta2.get_saldo()
print(f'A soma do saldo das contas é {soma}')

print(conta1.__dict__)
conta1.set_limite(99999999)
print(conta1.__dict__)
---------------------------------------------------

"""


class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    @property
    def valor_total(self):
        return self.__saldo + self.__limite


conta1 = Conta('Lana', 3000, 5000)
conta2 = Conta('Mitski', 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

nomes = conta1.titular + ' ' + conta2.titular
print(nomes)
print("")
soma = conta1.saldo + conta2.saldo  # Fazemos acesso sem os () mesmo sendo um método pelo uso do decorador @property
print(f'A soma do saldo das contas é {soma}')

print(conta1.__dict__)
conta1.limite = 212912
print(conta1.__dict__)

print(conta1.valor_total)
print(conta2.valor_total)

print('''\n''')

