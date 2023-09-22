"""
Teste de velocidade com Expressões Geradores
# Generators (Geradores)

def nums():
    for num in range(1, 10):
        yield num

# Generator Expression
# ge2 = (num for num in range(1, 10))


"""

# Teste de velocidade

import time

# Generator Expression

gen_inicio = time.time()
print(sum(num for num in range(500000000)))  # 100 milhões
gen_tempo = time.time() - gen_inicio

list_inicio = time.time()
print(sum([num for num in range(500000000)]))  # 100 milhões
list_tempo = time.time() - list_inicio

print(f'Generator Expression levou {gen_tempo}')  # 36.34315586090088
print(f'List Comprehension levou {list_tempo}')  # 104.23299765586853
