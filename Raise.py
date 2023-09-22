"""
Levantando erros com Raise

raise - Lança exceções

Raise não é uma função, é uma palavra reservada como def.
Útil para informar erros

Sintaxe:

raise TipoDoErro('Mensagem de erro')
Raise termina a função assim como Return
"""


def colore(texto, cor):
    cores = ['verde', 'amarelo', 'azul', 'branco']
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')

    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('coroação', 'vermelho')
