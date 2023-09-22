"""
Definindo Funções

- Funções são pequenos trechos de código que realizam tarefas específicas
- Pode ou não receber entraddas de dados e retornar uma saída de dados;
Muito úteis para executar procedimentos similares por repetidas vezes



Funções, exemplos:
print()
len()
max()
min()
count()

"""

#Função integradas são chamadas de built-in

"""
Forma geral de definir uma função:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao
    
Onde:
nome_da_funcao - Sempre com letras minúsculas, e se for composto, separado por underline
parametros_de_entrada: - Opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não
bloco_da_funcao - Também chamado de corpo da função ou implementaçãom é onde o processamento da função acontece.
Neste bloco, pode ter ou não retorno da função

def - informa que estamos definindo uma função

"""


def diz_oi():
    print("oi!")

diz_oi()

#Dentre funções pode-se utilizar outras funções
#Variáveis podem executar a função
diz = diz_oi
diz()
