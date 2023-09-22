"""
Geradores

- Geradores (generators) são Iterators(iteradores).
Nem todo iterator é um generator

Generators podem ser criados com funções geradires.
Funções geradoras utilizam a palavra reservada yield
Generators podem ser criados com Expressões Geradoras

Diferenças entre Funções e Generator Functions

------------------------------------------------------------------------------------
| Funções                                  | Generator Functions                   |
------------------------------------------------------------------------------------
| Utilizam return                          | Utilizam yield                        |
____________________________________________________________________________________
| Retorna uma vez                          | Podem utilizar yield múltiplas vezes  |
------------------------------------------------------------------------------------
| Quando executada, retorna um valor       | Quando executada, retorna um generator|
------------------------------------------------------------------------------------

"""


# Exemplo Função Geradora (Generator Function)

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

# Uma Generator Function não é um Generator. Ela gera um generator.


gen = conta_ate(10)

print(type(gen))

print(next(gen))

for num in gen:
    print(num)