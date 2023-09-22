"""
Escrevendo em arquivos

# Ao abrir um arquivo para leitura, não podemos realizar a escrita dele.
# Se abrirmos um arquivo para a escrita, não podemos lê-lo.
# Ao abrir um arquivo para a escrita, o arquivo é criado no sistema operacional
Para escrever dado em um arquivo, após abrir o arquivo utilizamos a função write
e essa função recebe uma string como parâmetro

Abrindo um arquivo p a escrita com o modo 'w', se o arquivo não existir ele será criado
caso ele já exista, o anterior será apagado e um novo será criado. Dessa forma, todo
o conteúdo no arquivo anterior é perdido

with open('novo.txt', 'w') as arquivo:
    arquivo.write('Tô com fome.\n')
    arquivo.write('E com sono.\n')
    arquivo.write('E escrevendo isso.\n')
-----------------------------
"""

with open('frutas.txt', 'w') as arquivo:
    while True:
        fruta = input('Digite uma fruta ou digite "sair" para sair: ')
        if fruta == 'sair':
            break
        else:
            arquivo.write(fruta + '\n')
