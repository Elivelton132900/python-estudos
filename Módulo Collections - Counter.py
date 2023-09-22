"""
Counter

Recebe um interável como parâmetro e cria um objeto do tipo Collections Counter que é parecida com um dicionário,
contendo como chave o elemento da lista passada como parâmetro e como o valor a quantidade de ocorrências
desse elemento

from collections import Counter

lista = [1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 2, 2, 2, 2, 4, 2, 2, 2, 4, 4, 4, 4, 2, 3, 3, 100]
res = Counter(lista)
print(res)

retorna o valor e as ocorrências que aparecem

"""

"""
from collections import Counter

texto = ""My God, I'm so lonely
So I open the window
To hear sounds of people
To hear sounds of people
Venus, planet of love
Was destroyed by global warming
Did its people want too much too?
Did its people want too much?
And I don't want your pity
I just want somebody near me
Guess I'm a coward
I just want to feel alright
And I know no one will save me
I just need someone to kiss
Give me one good honest kiss
And I'll be alright
Nobody, nobody, nobody
Nobody, nobody
Ooh, nobody, nobody, nobody
I've been big and small
And big and small
And big and small again
And still nobody wants me
Still nobody wants me
And I know no one will save me
I'm just asking for a kiss
Give me one good movie kiss
And I'll be alright
Nobody, nobody, nobody
Nobody, nobody
Ooh, nobody, nobody
Nobody, nobody, nobody
Nobody, nobody, nobody, nobody
Nobody, nobody, nobody, nobody
Nobody, nobody, nobody, nobody
Nobody, nobody
Nobody, nobody, no""
texto = texto.split()
res = Counter(texto)
print(res.most_common(5))

Retorna as 5 palavras mais comuns do texto, de acordo com o argumento
"""


from collections import Counter

texto = """My God, I'm so lonely
So I open the window
To hear sounds of people
To hear sounds of people
Venus, planet of love
Was destroyed by global warming
Did its people want too much too?
Did its people want too much?
And I don't want your pity
I just want somebody near me
Guess I'm a coward
I just want to feel alright
And I know no one will save me
I just need someone to kiss
Give me one good honest kiss
And I'll be alright
Nobody, nobody, nobody
Nobody, nobody
Ooh, nobody, nobody, nobody
I've been big and small
And big and small
And big and small again
And still nobody wants me
Still nobody wants me
And I know no one will save me
I'm just asking for a kiss
Give me one good movie kiss
And I'll be alright
Nobody, nobody, nobody
Nobody, nobody
Ooh, nobody, nobody
Nobody, nobody, nobody
Nobody, nobody, nobody, nobody
Nobody, nobody, nobody, nobody
Nobody, nobody, nobody, nobody
Nobody, nobody
Nobody, nobody, no"""


separado = texto.split(" ")


res = Counter(separado)
print(res)