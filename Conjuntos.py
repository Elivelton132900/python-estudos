"""
Conjuntos são também chamados de Sets

Sets não possuem valores duplicados
Sets não possuem valores ordenados
Elementos não são acessados via índice, ou seja, conjuntos não são indexados

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos com a ordenação
deles. Quando não precisamos nos preocupar com chaves, valores e itens duplicados

Sets são referenciados em Python com chaves {}
Diferenças entre Set e Mapas:
    Um dicionário tem chave/valor
    Um conjunto tem apenas valor

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})
print(s)
Não aparecerá valores repetidos e não retornará erros
"""

"""
s.add(4) - Adiciona um valor ao conjunto
s.remove(2) - Remove um valor do conjuunto (Não é o índice, pq conjuntos não são indexados). Nenhum valor é retornado.
s.discard(22) - Se o valor do argumento não existir no conjunto, ele não remove nada e não é gerado erro
s.clear() - Limpa o conjunto
----------------------------
s = {1, 2, 3}  #Deep Copy (Alterar um conjunto não altera o outro)
novo = s.copy()
print (f"s: {s} novo: {novo}")
novo.add(4)
print (f"s: {s} novo: {novo}")
-------------------------------
s = {1, 2, 3} #Shallow Copy (Alterar um conjunto altera o outro)
novo = s
print (f"s: {s} novo: {novo}")
novo.add(4)
print (f"s: {s} novo: {novo}")
-------------------------------

-------------------------------------------------------------------------
estudantespython = {'Julia', 'Ana', 'Paulo', 'Ellen', 'Pedro', 'Joana'}
estudantesjava = {'Julia', 'Guilherme', 'Rayhan', 'Joana', 'Pedro'}
estudantesunicos = estudantespython.union(estudantesjava)
print(estudantesunicos)
                                                                                   #Retorna os estudantes sem repetir os nomes dos que estão fazendo duas classes
estudantespython = {'Julia', 'Ana', 'Paulo', 'Ellen', 'Pedro', 'Joana'}            #UNIÃO
estudantesjava = {'Julia', 'Guilherme', 'Rayhan', 'Joana', 'Pedro'} 
estudantesunicos = estudantespython | estudantesjava
print(estudantesunicos)
----------------------------------------------------------------------------
estudantespython = {'Julia', 'Ana', 'Paulo', 'Ellen', 'Pedro', 'Joana'}
estudantesjava = {'Julia', 'Guilherme', 'Rayhan', 'Joana', 'Pedro'}            #Retorna os estudantes que estão em ambas as classes
ambos = estudantespython.intersection(estudantesjava)                          #INTERSECÇÃO
print(ambos)

estudantespython = {'Julia', 'Ana', 'Paulo', 'Ellen', 'Pedro', 'Joana'}
estudantesjava = {'Julia', 'Guilherme', 'Rayhan', 'Joana', 'Pedro'}
ambos = estudantespython & estudantesjava
print(ambos)
--------------------------------------------------------------------------
estudantespython = {'Julia', 'Ana', 'Paulo', 'Ellen', 'Pedro', 'Joana'}
estudantesjava = {'Julia', 'Guilherme', 'Rayhan', 'Joana', 'Pedro'} 
sopython = estudantespython.difference(estudantesjava)             #Retorna Apenas os estudantes que fazem apenas aquela aula
sojava = estudantesjava.difference(estudantespython)                #DIFERENÇA
print(sojava, sopython)

"""

"""
sum(s) - Soma do conjunto
max(s) - Maior valor do conjunto
min(s) - Menor valor do conjunto
len(s) - Tamanho do conjunto
"""
