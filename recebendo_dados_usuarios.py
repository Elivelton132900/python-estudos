""""
-------------Exemplo versão antiga
print("Qual seu nome?")
nome = input()
print("Seja bem-vindo(a, e) %s" % nome)
print("Qual sua idade?")
idade = input()
print("%s tem %s anos." % (nome, idade))
"""


""""
------------Exemplo mais atual
print("Qual seu nome?")
nome = input()
print("Seja bem-vindo(a,e), {0}".format(nome))
print("Qual sua idade?")
idade = input()
print("{0} tem {1} anos.".format(nome, idade))
"""


"""
print("Qual seu nome?")
nome = input()
print(f"Seja bem-vindo(a,e),{nome}")
print("Qual sua idade?")
idade = input()
print(f"{nome} tem {idade} anos.")
print(f"{nome} nasceu em {2020 - int(idade)}).")
"""

nome = input("Qual seu nome? \n")
print(f"Bem vindo(a,e) {nome}.")
idade = int(input("Qual sua idade? \n"))
print(f"{nome} tem {idade} anos. \n" f"{nome} nasceu em {(2020 - idade)}.")