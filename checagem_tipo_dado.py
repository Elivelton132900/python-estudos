import math

# Type Hinting

def cumprimentar(nome: str) -> str:
    return f'Olá, {nome}'


print(cumprimentar('Elivelton'))


# type hinting
def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '*')


# print(cabecalho('elivelton'))
# print(cabecalho('elivelton', alinhamento=False))


# Executando o script com 'erro'
# mypy nome_arquibvo.py
# print(cabecalho('elivelton', alinhamento='geek'))
# checagem_tipo_dado.py:22: error: Argument "alinhamento" to "cabecalho" has incompatible type "str";
#  expected "bool"


# Correto

nome_pessoa: str = 'Kátia'
idade_pessoa: int = 29
cor_pessoa: str = 'Amarela'


class Pessoa:

    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.__nome: str =  nome
        self.__idade: int = idade
        self.__peso: float = peso

    def andar(self) -> str:
        return f'{self.__nome} está andando'


p = Pessoa(nome='Geek', idade=32, peso=69.3)

# ------------------------------------------------------------


def circunferencia(raio):
    # type: (float) -> float
    return 2 * math.pi * raio


def cabecalho2(texto, alinhamento=True):
    # type: (str, bool) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'


def cabecalho3(
        texto,  # type: str
        alinhamento=True # type: bool
): # type: (...) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'


apelido = 'Lili'  # type: str
