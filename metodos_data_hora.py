"""
Métodos de Data e Hora

import datetime
agora = datetime.datetime.now()  # Podemos especificar o timezone nesse método
print(agora)
print(type(agora))
print(repr(agora))
print("")
hoje = datetime.datetime.today()  # Não podemos especificar timezone nesse método
print(hoje)
print(type(hoje))
print(repr(hoje))
------------------------------------------------------------------------
import datetime

# Mudanças ocorrendo à meia-noite combine()

manutencao = datetime.datetime.combine(datetime.datetime.now() + datetime.timedelta(days=1), datetime.time())
print(manutencao)
--------------------------------------------------------------------------

import datetime

# Encontrar o dia da semana weekday()
# Os dias da semana do método weekday() começam em 0, e 0 = segunda-feira
manutencao = datetime.datetime.combine(datetime.datetime.now() + datetime.timedelta(days=1), datetime.time())
print(manutencao.weekday())
-----------------------------------------------------------------------------
import datetime

aniversario = input('Qual sua data de nascimento (dd/mm/yy) ')
aniversario = aniversario.split('/')
aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))

dias_semana = ['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feita', 'sexta-feira', 'sábado', 'domingo']

for indice, dia in enumerate(dias_semana):
    if indice == aniversario.weekday():
        print(f'Você nasceu numa {dias_semana[indice]}')
---------------------------------------------------------------------------
import datetime

# Formatando data/hora com strftime() (string format time)

hoje = datetime.datetime.today()
print(hoje)

hoje_formatado = hoje.strftime('%d/%m/%Y')  # y minusculo = ano em dois dígitos | Y maiúsculo = ano em 4 dígitos
print(hoje_formatado)
---------------------------------------------------------------------------
import datetime

# Formatando data/hora com strftime() (string format time)

hoje = datetime.datetime.today()
print(hoje)

hoje_formatado = hoje.strftime('%d de %B de %Y')  # B maiúsculo = mês formatado e completo, porém em ingês.
# b minúsculo = mês formatado e abreviado, porém em inglês
print(hoje_formatado)
-------------------------------------------------------------------------
import datetime

nascimento = input('Qual sua data de nascimento? (dd/mm/yyyy) ')
nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y')
print(nascimento)
------------------------------------------------------------------------
import datetime

# Somente a hora

almoco = datetime.time(12, 30, 0)
print(almoco)
-------------------------------------------------------------------------
import timeit

# Marcando tempo de execução do nosso código com timeit
# Loop for
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(tempo)

# List Comprehension
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(tempo)

# Map
tempo = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(tempo)

--------------------------------------------------------------------------
"""


import timeit
import functools


def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4 ** num
    return soma


print(timeit.timeit(functools.partial(teste, 5), number=10000))
# functools.partial() recebe como parametro a funcao e os argumentos dessa função.
# Assim, é possível testar se essa função é perfomática ou não
