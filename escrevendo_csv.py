"""
Escrevendo em arquivos CSV

reader() (leitor), writer() (escritor)

writewor - Escreve uma linha
--------------------------------------------------------
# writer() Gera um objeto para que possamos escrever em um arquivo CSV, utilizamos o método
# writerow() para escrever cada linha. Este método recebe uma lista.

from csv import writer

with open('filmes.csv', 'w', encoding='UTF-8', newline='') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Título', 'Gênero', 'Duração'])
    while filme != 'sair':
        filme = input('Informe o nome do filme ')
        if filme != 'sair':
            genero = input('Informe o gênero ')
            duracao = input('Digite a duração do filme em minutos ')
            escritor_csv.writerow([filme, genero, duracao])
--------------------------------------------------------

"""


# DictWriter
# As chaves do dicionário devem ser as mesmas utilizadas no cabeçalho

from csv import DictWriter

with open('filmes_dic.csv', 'w', encoding='UTF-8', newline='') as arquivo:
    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Digite o nome do filme ')
        if filme != 'sair':
            genero = input('Informe o gênero ')
            duracao = input('Informe a duração em minutos ')
            escritor_csv.writerow({'Título': filme, 'Gênero': genero, 'Duração': duracao})

