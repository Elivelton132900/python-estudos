nome_criacao = input('Digite o nome do arquivo para armazenar a informação do tipo "cidade:num_habitantes" ')
extensao = '.txt'
cidade = ''

with open(f'{nome_criacao}{extensao}', 'w+', encoding='UTF-8') as arquivo:
    while cidade != '0':
        cidade = input('Digite o nome da cidade seguido de ":". [0 para sair] ')
        habitantes = input('Digite o número de habitantes. não há necessidade de espaçamento ')
        if ':' in cidade and ' ' not in habitantes:
            arquivo.write(cidade)
            arquivo.write(habitantes)
            arquivo.write("\n")
