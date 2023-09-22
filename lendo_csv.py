"""
Lendo Arquivos CSV

CSV - Comma Separeted Values (Valores separados por vírgulas)

# Separador por vírgula

1, 2, 3, 4, 5, 6

'Geek', 'University', 'python', 'ciencia', 'dados'

# Separador por ponto e vírgula
1; 2; 3; 4; 5; 6

'Geek'; 'University'; 'python'; 'ciencia'; 'dados'

# Separador por espaço
1 2 3 4 5 6

'Geek' 'University' 'python' 'ciencia' 'dados'

# Possível de se trabalhar mas não é o ideal

with open('lutadores.csv', encoding='utf-8') as arquivo:
    dados = arquivo.read()
    # print(type(dados))
    dados = dados.split(',')[2:]
    print(dados)

A linguagem Python possui duas formas diferentes para ler dados em arquivos csv
    - reader - Permite que iteremos sobre as linhas do arquivo CSV como listas;
    - DictReader - Permite que iteremos sobre as linahs do arquico CSV como OrderedDicts;
-------------------------------------------------------------------------------
# Reader

from csv import reader

with open('lutadores.csv', encoding='UTF-8') as arquivo:
    leitor_csv = reader(arquivo)  # iterator
    next(leitor_csv)
    for linha in leitor_csv:
        print(f'{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]} cms')
--------------------------------------------------------------------------------
from csv import DictReader

with open('lutadores.csv', encoding='UTF-8') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu no(a) {linha['País']} e mede {linha['Altura (em cm)']} cm")
"""


# Com outro separador

from csv import DictReader

with open('lutadores.csv', encoding='UTF-8') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu no(a) {linha['País']} e mede {linha['Altura (em cm)']} cm")