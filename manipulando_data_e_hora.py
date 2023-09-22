"""
Manipulando Data e Hora

Python tem um método builtin para se trabalhar com data e hora
chamado datetime
-------------------------------------------------------------
import datetime

print(datetime.MAXYEAR)
print(datetime.MINYEAR)

# Retorna data e hora corrente  |  2021-01-16 18:17:33.663249

# datetime.datetime(2021, 1, 16, 18, 18, 24, 414863)
print(repr(datetime.datetime.now()))

# replace() para fazer ajustes na data/hora

inicio = datetime.datetime.now()
print(inicio)

# Alterar o horário para 16 horas, 0m, 0s, 0ms
inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)
print(inicio)
-------------------------------------------------------------
# Recebendo dados e transformando em datas
import datetime

evento = datetime.datetime(2021, 1, 17, 0)
print(type(evento))
print(evento)

nascimento = input('Informe sua data de nascimento (dd/mm/yy) ')
nascimento = nascimento.split('/')
nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))
print(nascimento)
print(type(nascimento))
--------------------------------------------------------------
"""


import datetime

evento = datetime.datetime.now()
# Acesso individual dos elementos de data e hora

print(evento.year)
print(evento.month)
print(evento.day)
print(evento.hour)
print(evento.minute)
print(evento.second)
print(evento.microsecond)