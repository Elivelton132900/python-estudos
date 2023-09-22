"""
Por que testar nosso código?
Testes automatizados!
        - Reduzir bugs
        - Testes garantem que novos recursos da aplicação não quebrem recursos antigos
        - Testes garantem que bugs corrigidos anteriormente continuem corrigidos
        - Testes garantem que a refatoração não traga novos bugs


              Aplicação Web
|---------------------------------------|
|           frontend e backend          |
|.......................................|
|           testes automatizados        |
|_______________________________________|

TDD - Test Driven Development (Desenvolvimento Guiado por Testes)
Com TDD é utilizado estágios de desenvolvimento
       - Você escreve seu teste primeiro
       - Então você escreve o código mínimo suficiente para fazer o teste passar (ou seja, executar com sucesso)
       - Então refatora o código para realizar a funcionalidade e testa novamente
       - Uma vez que o teste passe, o recurso é considerado completo

Estes estágios de desenvolvimento do TDD são quase como um mantra que os desenvolvedores seguem, conhecidos como:
       - Red       - Quando o teste dá errado
       - Green     - Quando o teste passa
       - Refactor
"""


class Gato:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'{self.__nome} está miando...')


felix = Gato('Felix')
felix.miar()
print(felix.nome)
