"""
Default Dict


Ao criar um dicionário utilizando-o, nós informamos um valor default,
podendo utilizar um lambda para isso. Este valor será utilizado sempre que não houver
um valor definido. Caso tentemos acessar uma chave que não existae, essa chave será
criada e o valor default será atribuído

Obs: Lambda são funções sem nome, que podem ou não receber parâmetros de entrada e retornar valores.
"""

from collections import defaultdict

dicionario = defaultdict(lambda:0)
dicionario['curso'] = 'Programação em Python: Essencial'
print(dicionario)
print(dicionario['outro']) # KeyError no dicionário comum, mas aqui não.
print(dicionario)