"""
POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico e hierárquico utilizanndo
classes

Encapsular - cápsula

            classe
   -----------------------------
  |       Atributos e Métodos   |
   ----------------------------

# Relembrando Atributos/Métodos privados em Python

Imagine que temos uma classe chamada Pessoa contendo um atributo
privado chamado __nome e um método pricado chamado __falar(self)

Esses elementos privados só devem/deveriam ser acessados dentro da classe.
Mas Python não bloqueia este acesso fora da classe. Com Python acontece um
fenômeno chamado Name Mangling, que faz uma alteração na forma de se acessar
os elememntos privados. Conforme:

_Claasse__elemento

Exemplo - Acesando elementos privados fora da classe:
instancia._Pessoa__nome
instancia._Pessoa__falar()

Abstração em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atirbutos e métodos
privados de usuário


"""


class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

"""
conta1 = Conta('Lana', 150.00, 1500)

# Como os atributos públicos é possível fazer alterações, tornando-os assim inseguro
print(conta1.numero)
print(conta1.titular)
print(conta1.saldo)
print(conta1.limite)

conta1.numero = 42
conta1.titular = 'Xuxa'
conta1.saldo = 99999999999999999
conta1.limite = 9000000000000000000000000

print(conta1.__dict__)
conta1.extrato()
"""