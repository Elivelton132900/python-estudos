"""
Poo - Classes

Em POO, Classes nada mais são do que modelos de objetos do mundo real sendo representados
computacionalmente.

Imagine que você queira fazer um sistema para automatizar o controle das lâmpadas da sua casa

Classes podem conter:
    - Atributos: representam as características do objeto. Ou seja, pelos atributos, conseguimos
representar computacionalmente os estados de um objeto. No caso da lampada. possivelmente iríamos querer
saber se a lâmpada é 1220 ou 220 w, se ela é branca, amarela, vermelha ou alguma outra cor, qual a luminosidade e etc

    - Métodos (funções): Representam os comportamentos do objeto, ou seja, as ações que este objeto
    pode realizar no seu sistema. No caso da lâmpada, por exemplo, um comportamento comum que
    muito provavelmente iríamos querer representar no nosso sistema é o de ligar e desligar
    a mesma.

Em Python, para definir uma classe utilizamos a palavra reservada class.

obs: Utilizamos a palavra 'pass' em Python quando temos um bloco de código que ainda não está
implementado.
obs: Quando nomeamos uma classe em Pyhton utilizamos por convenção o nome com inicial
em maiúsculo. Se o nome for composto, utiliza-se as iniciais de ambas as palavras em
maiúsculo, todas juntas

obs: Quando estamos planejando um software e definimos quais classes teremos que ter no sistema, chamamos
estes objetos que serão mapeados para classes de entidade
"""


class Lampada:
    pass


lamp = Lampada()
