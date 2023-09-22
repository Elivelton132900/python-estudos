"""
Sistema de Arquivos - Manipulação

# Procurando arquivo em diretório
# Diretório
# Paths relativo
print(os.path.exists('geek'))
print(os.path.exists('geek/university'))
-------------------------------------

import os


# Criando arquivos

# forma 1
open('arquivo-teste.txt', 'w').close()

#forma 2
open('arquivo-teste2', 'a').close()

# forma 3
with open('arquivo-teste3.txt', 'w') as arquivo:
    pass  # Usado para simbolizar que não haverá nada no bloco e para não retornar erro de identação
------------------------------------
import os

os.mknod('arquivo-teste4.txt')
os.mknod('/home/geek/univertisy.txt')  # Não funciona por ser Windows.
------------------------------------
import os

# Path Relativo
os.mkdir('templates')  # A função mkdir() cria um diretório se este não existir, caso exista, retorna erro
# Se não tivermos permissão para criar o diretório, retorna PermissionError
os.makedirs('templates/geek/university')  # Criando múltiplos diretórios
os.makedirs('templates/geek/university', exist_ok=True)  # Se já houver os diretórios, não retorna erro
-------------------------------------
import os

os.rename('templates', 'geek2')  # Renomeia diretório
------------------------------------
import os

os.rename('texto.txt', 'geek.txt')  # Renomear arquivos
--------------------------------------
import os

os.remove('geek.txt')  # Remove um arquivo
---------------------------------------
import os

os.rmdir('templates')  # Remove um diretório
# Se o diretório ter arquivo, retornará erro.
----------------------------------------
import os

os.removedir('x, x, x, x,')  # Remove diretórios vazios
-----------------------------------------
"""


