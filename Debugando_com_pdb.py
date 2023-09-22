"""
Debuggando com PDB

PDB -> Python Debugger

# Prática RUIM
def dividir(a, b):
    print(f'A: {a}, B? {b}')
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Valor incorreto: {err}'
------------------------------------

import pdb

pdb.set_trace() = Marca um breakpoint

comandos:
l (listas onde estamos)
n (próxima linha)
p (próxima variável)
c (continua a execução)

import pdb; pdb.set_trace() = importa direto numa linha


A partit do Python 3.7 não é mais necessário importar uma biblioteca. O breakpoint foi incorporado como uma função built-in
breakpoint()

caso o nome das variáveis sejam os mesmos dos comandos pdb, é necessário usar (p, p(print p)) para imprimir as variáveis
e nõo executar os comandos
"""



