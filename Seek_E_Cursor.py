"""
Seek e Cursor

seek() - É utilizada para movimentar o cursor pelo arquivo

arquivo = open('texto.txt')
print(arquivo.read())

# seek() - é utilizada para a movimentação do cursos pelo arquivo
# O parâmetro indica onde o cursor estará
# Movimentando o cursor pelo arquivo com a função seek()
arquivo.seek(0)
print(arquivo.read())
-----------------------------
# readline() - função que lê o arquivo linha por linha

arquivo = open('texto.txt')
print(arquivo.readline())
------------------------------
arquivo = open('texto.txt')
linhas = arquivo.readlines()
print(len(linhas))
------------------------------
arquivo = open('texto.txt')
# Quando abrimos um arquivo com a função open() é criado uma conexão entre o arquivo no disco do computador e o nosso
# Programa. Essa conexão é chama de streaming. Ao finalizar o trabalho com o arquivo, devemos fechar essa conexão.
# Utilizamos a função close() para isso.
print(arquivo.read())
print(arquivo.closed) # Retorna False se o arquivo estiver aberto e True caso estiver fechado
arquivo.close()
print(arquivo.closed)
# Útil para não retornar ValueError.
-----------------------------
arquivo = open('texto.txt')
print(arquivo.read(4))  # Limita a quantidade de caracteres a ser lidos
-----------------------------
"""



with open('C:\\Users\\Elivelton\\PycharmProjects\\Exercicios\\arq_at_4.txt') as texto:
    print(texto.read())
