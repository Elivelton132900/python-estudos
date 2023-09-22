"""
Lambdas

Lambdas são funções sem nomes, ou funções anônimas

def funcao(x):
    return 3 * x + 1

# lambda x: 3 * x + 1
# Utilizando a expressão:


calc = lambda x: 3 * x + 1
---------------------------------------
# Expressões lamba com múltiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip() + " " + sobrenome.strip().title()
# strip() = Remove os espaços no início e no fim da variável, se tiver só um ele retira só um


print(nome_completo('   lana', '   DEL REY '))
-----------------------------------------

# Lambdas pode ter nenhuma ou várias entradas

amar = lambda: 'Como não amar Python'

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** 0.5

tres =  lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

print(amar())
print(uma(6))
print(duas(5, 6))
print(tres(3, 6, 9))
-----------------------------------------
autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Helbert'
           'Orson Scott Card', 'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']

print(autores)
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)



# Parâmetros a mais ou faltando retorna erro

"""





