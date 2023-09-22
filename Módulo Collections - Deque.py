"""
Módulo Collections - Deque

Lista de alta performance
"""

from collections import deque

deq = deque ('geek')
print(deq)
deq.append('y')
print(deq)
deq.appendleft('k')
print(deq) #Adiciona no começo
#Remover elementos

print(deq.pop()) #remova e retorna o último elemento
print(deq)
print(deq.popleft()) # Remove e retorna o primeiro elemento da lista
print(deq)