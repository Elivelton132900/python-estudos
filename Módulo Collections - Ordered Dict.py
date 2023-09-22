"""
Ordered Dict

É um dicionário que nos garanta a ordem de inserção dos elementos

from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e':5})
"""
from collections import OrderedDict

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 1, 'a': 2})

print(odict1 == odict2)

#Retorna False porque para o OrderedDict importa a ordem.


