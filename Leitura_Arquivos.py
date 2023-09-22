"""
Leitura de Arquivos

Para ler o contéudo de um arquivo, utiliza-se a função open()

open() - Passa apenas um parâmetro de entrada obrigatório, que é o arquivo a ser lido.
essa função retorna '_io.TextIOWrapper. usa-se ele para trabalhar.

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>
mode r - Modo de leitura
"""

arquivo = open('texto.txt')

ret = arquivo.read()
print(ret)
print(type(ret))  # Retorna uma string
# print(arquivo)
# print(type(arquivo))

# print(arquivo.read())
# print(arquivo.read())  # Python utiliza um arquivo chamado cursos. Esse cursor
# funciona como o cursor quando estamos escrevendo
