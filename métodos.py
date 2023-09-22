"""
POO - Métodos

Métodos (funções) - Representam os comportamentos do objeto. Ou seja, as ações
que este objeto pode realizar no seu sistema

Em Python, dividimos os métodos em dois grupos:
          - Métodos de Instância
          - Métodos de Classe

#  Métodos de Instância

O método __init__ é um método especial chamado de construtor e
sua função é construir o objeto a partir da classe.
Todo elemento em Python que inicia e termina com duplo _ é chamado de dunder
Os métodos/funções dunder em Python são chamados de métodos mágicos

Por mais que possamos criar nossas próprias funções utilizando dunder (_ no início e fim)
não é aconselhado. Python possui vário métodos com esta foema de nomenclatura e pode ser que mudemos o
comportamento dessas funções mágicas internas da linguagem. Então, evite ao máximo. De preferência, nunca o faça

Métodos são escritos em letras minúsculas. Se o nome for composto, o nome terá as palavras separadas por underline.

nome = input('Informe o nome ')
sobrenome = input('Informe o sobrenome ')
email = input('Informe o email ')
senha = input('Digite a senha ')
confirma_senha = input('Confirme a senha ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senhas não idênticas')
    exit(1)

print('Usuário criado com sucesso!')
senha = input('Digite a senha para acesso ')

if user.checa_senha(senha):
    print('Acesso permitido')
else:
    print('Acesso negado')

print(f'Senha criptografada: {user._Usuario__senha}')  # Acesso errado

-----------------------------------------------------------------------------------------

"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com o desconto"""
        return (self.__valor * (100 - porcentagem)) / 100


from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:

    contador = 0

    @classmethod  # utilizado para fazer um método de classe
    def conta_usuarios(cls):
        print(f'Temos {cls.contador} usuário(s) no sistema')

    @staticmethod  # Método estático
    def definicao():
        return 'UXRL344'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1  # Atributo de instância
        self.__nome = nome  # Atributo de instância
        self.__sobrenome = sobrenome  # Atributo de instância
        self.__email = email  # Atributo de instância
        self.__senha = cryp.hash(senha, rounds=200000)  # Atributo de insância
        Usuario.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario()}')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'  # Faz acesso a atributos da instância, por isso é um método de inst

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):  # Faz acesso a atributos de instancia, por isso é um metodo de instância
            return True
        return False

    def __gera_usuario(self):  # Método privado, não é possível utilizá-lo fora da classe
        return self.__email.split('@')[0]


# Métodos de classe

# user = Usuario('Elivelton', 'Silva', 'elivelton1329@gmail.com', '123456')

# Usuario.conta_usuarios()  # Forma correta
# user.conta_usuarios()  # Possível, porém incorreto

# Criamos métodos de instância quando esses metodos precisam fazer acesso à atributos de instância
# Criamos métodos de classe quando não precisamos fazer acesso a atributos de instância

# print(user._Usuario__gera_usuario())  # Forçando acesso ao método privado


# Métodos estáticos

print(Usuario.contador)
print(Usuario.definicao())
print("")
user2 = Usuario('Lana', 'Del rey', 'lanadelrey@gmail.com', 'minhasenha123')

print(user2.contador)
print(user2.definicao())
