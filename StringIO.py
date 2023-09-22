"""
StringIO

Para ler ou escrever dados em arquivos do sistema operacional, o software
precisa ter permissao:
- De leitura
- De Escrita

StringIO - Utilizado para ler e criar arquivos em memória
"""

# import

from io import StringIO

mensagem = 'String Normal '

# Podemos criar um arquivo em memória já com uma string inserida ou mesmo vazio para inserirmos texto depois
arquivo = StringIO(mensagem)
print(arquivo.read())
# Agora tendo o arquivo, podemos utilizar as mesmas funções.
arquivo.write('Outro Texto')
arquivo.seek(0)
print(arquivo.read())
