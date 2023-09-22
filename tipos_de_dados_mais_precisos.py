"""
int, str, float, list, set, dict, etc
"""

"""
----------------------------------------------------------------------------------
- Literal type
Ajuda na checagem com o mypy
from typing import Literal


# def pegar_status(usuario: str) -> Literal['conectado', 'desconectado']:
#     pass


def calcula_v1(operacao: str, num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    else:
        raise ValueError(f'Operação inválida {operacao!r}')  # !r apresenta a operacao entre aspas simples


def calcula_v2(operacao: Literal['+', '-'], num1: int, num2:int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    else:
        raise ValueError(f'Operação inválida {operacao!r}')  # !r apresenta a operacao entre aspas simples


calcula_v2('+', 6, 4)
calcula_v2('-', 10, 2)
calcula_v2('*', 3, 5)


- Union
from typing import Union


def soma(num1: int, num2: int) -> Union[str, int]:  # Pode-se usar nos argumentos também, por exemplo,
    # num1: Union[float, int]
    resultado: int = num1 + num2

    if resultado > 50:
        return f'O valor {resultado} é muito grande'
    else:
        return resultado
----------------------------------------------------------------------------

- Final
from typing import Final


NOME: Final = 'Geek'
print(NOME)

# NOME = 'GEEK'
# print(NOME)   error: Cannot assign to final name "NOME" <- Checando com mypy
---------------------------------------------------------
Podemos importar final com f minúsculo para decorar métodos.
Decorando método, não poderia ser possível sobreescrevê-la em alguma
outra classe caso for herdada.
Também não poderia ser possivel herdá-la. (mypy)

from typing import final

@final
class Pessoa:
    pass
    
    
class Estudante(Pessoa):
    pass
    
    @final
    def estudar(self)
        print('Estou estudando...')
        

class Estagiario(Estudante):
    pass
    
    def estudar(self):
        print('Estudando e estagiando...')
----------------------------------------------------------------------------------
- Typed dictionaries

from typing import TypedDict


class CursoPython(TypedDict):
    versao: str  # Retorna o atributo com o objeto instanciado em forma de dicionário
    atualizacao: int


geek = CursoPython(versao='3.8.5', atualizacao=2020)
print(geek)  # {'versao': '3.8.5', 'atualizacao': 2020}
----------------------------------------------------------------------------
- Protocols
"""


from typing import Protocol


class Curso(Protocol):
    titulo: str


def estudar(valor: Curso) -> None:
    print(f'Estou estudando o curso {valor.titulo}')


class Venda:
    titulo = 'oi'


v1 = Venda()
estudar(v1)
