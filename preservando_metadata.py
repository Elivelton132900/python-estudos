"""
Preservando metadatas com wraps

Metadados - São dados intrísecos em arquivos.
Wraps - São funções que envolvem elementos com diversas finalidades.

def ver_log(funcao):
    def logar(*args, **kwargs):
        # Eu  sou uma função (logar) dentro de outra
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    # Soma dois números
    return a + b


# print(soma(10, 30))
print(soma.__name__)  # soma, porém retorna logar
print(soma.__doc__)  # soma dois números, porém retorna a documentação da função logar
---------------------------------------------------------------------
"""


from functools import wraps


def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu  sou uma função (logar) dentro de outra"""
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois números"""
    return a + b


# print(soma(10, 30))
print(soma.__name__)  # soma, porém retorna logar
print(soma.__doc__)  # soma dois números, porém retorna a documentação da função logar

