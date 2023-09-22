"""
Sistema de naveação

Para navegar usando python, é necessário o uso do módulo os

import os

print(os.getcwd())  # Imprime o diretório atual em que estamos
os.chdir('..')  # Volta um diretório
---------------------------
import os


print(os.path.isabs('C:\\Users\\Elivelton'))  # No Windows
# Retorna se um path é absoluto ou relativo (False = relativo / True = absoluto)
---------------------------
import os

print(os.getcwd())

res = os.path.join(os.getcwd(), 'geek', 'university')

os.chdir(res)

print(os.getcwd())

# os.path.join() recebe dois parâmetros, sendo o diretório atual e o segundo o diretório que será juntado
# ao atual
---------------------------
import os

# Podemos listar os arquivos e diretórios com o listdir()
print(os.listdir('C://'))


"""


import os
# Podemos listar os arquivos e diretórios com mais detalhes com scandir()

scanner = os.scandir()
arquivos = list(scanner)
# print(dir(arquivos[0]))

print(arquivos[0].inode())  # Identificador do elemento na árvore de diretório
print(arquivos[0].is_dir())  # É um diretório?
print(arquivos[0].is_file())  # É um arquivo?
print(arquivos[0].is_symlink())  # É um link simbólico?
print(arquivos[0].name)  # Nome do arquivo
print(arquivos[0].path)  # Caminho até o arquivo
print(arquivos[0].stat())  # Estatística

# É necessário fechar a função scandir() assim quando abrimos um arquivo

scanner.close()
