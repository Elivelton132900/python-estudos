"""
POO - Atributos

Atributos - Representam as características do objeto. Ou seja, pelos atributos
nós conseguimos representar computacionalmente os estados de um objeto.


Em Python, dividimos os atributos em 3 grupos:
    - Atributos de Instâncias
    - Atributos de Classe
    - Atributos Dinâmicos

# Atributos de instância: São atributos declarados dentro do método construtor

Obs: É um método especial utilizado para a construção do objeto

Em Python, por convenção, ficou estabelecido que todo atributo de uma classe é público.
Ou seja, pode ser acessado em todo o projeto.
Caso queiramos demonstrar que determiando atributo deve ser tratado como privado, ou seja,
que deve ser acessado/utilizado somente dentro da própria classe onde está declarado,
utiliza-se __ duplo underscore no início de seu nome.

Isso é conhecido também como Name Mangling
--------------------------------------------------------------------------
# Isso é apenas uma convenção, ou seja, a linguaguem não
# vai impedir que façamos acesso aos atributos sinalizados como privados fora da classe.


user = Acesso('elivelton1329@gmail.com', '123456')
print(user.email)
# print(user.__senha)  # AttributeError: 'Acesso' object has no attribute '__senha'
print(user._Acesso__senha)  # Temos acesso mas não deveríamos fazer esse acesso. (Name Mangling)
user.mostra_senha()
-----------------------------------------------------------------------------
# Atributos de instancia significa que ao criarmos instâncias/objetos de uma classe,
# Todas as instancias terão estes atributos

user1 = Acesso('eliveltinho@gmail.com', '123456')
user2 = Acesso('eliveltim@gmail.com', '654321')

user1.mostra_email()
user2.mostra_email()
------------------------------------------------------------------------------
# Atributos de classe


# Atributos de classe, são atributos que são declarados diretamente na classe,
# ou seja, fora construtor. Geralmente já inicializamos um valor, e este valor é compartilhado
# entre todas as instâncias da classe. Ou seja, ao invés de cada instância da classe ter seus
# próprios valores como é o caso dos atributos de instância, com os atributos de classe todsas as instâncias
# terão o mesmo valor para este atributo

p1 = Produto('Playstation 4', 'Video game', 2300)
p2 = Produto('Xbox S', 'Video game', 4500)

print(p1.valor)  # Acesso possível porém errado de um atributo de classe
print(p2.valor)  # Acesso possível porém errado de um atributo de classe

# Não precisamos criar uma instancia de uma classe para fazer acesso a um atributo de classe

print(Produto.imposto)  # Acesso correto de um atributo de classe
print(p1.id)
print(p2.id)

# Em linguaguens como Java, os atributos conhecidos como atributos de classe aqui em Python
# São chamados de atributos estáticos
-----------------------------------------------------------------------------

"""


# Classes com Atributo de Instâncias Públicos

class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Atributos Públicos e Atributos Privados

class Acesso:

    def __init__(self, email, senha):
        self.email = email  # atributo publico
        self.__senha = senha  # atributo privado

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)



class Produto:

    # Atributo de classe
    imposto = 1.05  # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1  # Atributo de instância
        self.nome = nome  # Atributo de instância
        self.descricao = descricao  # Atributo de instância
        self.valor = (valor * Produto.imposto)  # Atributo de instância
        Produto.contador = self.id


# Atributos Dinâmicos - Um atributo de instância que pode ser criado em tempo de execução
# Obs: O atributo dinâmico será exclusivo da instância que o criou

p1 = Produto('Playstation 4', 'Video game', 2300)
p2 = Produto('Arroz', 'Mercearia', 5.99)

# Criando um atributo dinâmico em tempo de execução

p2.peso = '5KG'  # Na classe Produto não existe o atributo peso
print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}')
# print(f'Produto: {p1.nome}, Descrição: {p1.descricao}, Valor: {p1.valor}, Peso: {p1.peso}')  # Erro, não há o atributo
# 'PESO' na instância P1

# Deletando atributos

print(p1.__dict__)
print(p2.__dict__)
print("")

del p2.peso
del p2.valor
del p2.descricao

print(p1.__dict__)
print(p2.__dict__)
