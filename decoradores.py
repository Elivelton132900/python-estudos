"""
Decoradores (Decoratos)

- Decorators são funções
- Decorators envolvem outras funções e aprimoram seus comportamentos
- Decoratos também são exemplos de Higher Order Functions
- Decorators tem una sintaxe própria, usando '@' (Syntact Sugar / Açucar Sintático)

# Decorators como funções (Sintaxe não recomendada / Sem açucar Sintético)

def seja_educado(funcao):
    def sendo():
        print('Foi um prazer te conhecer!')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo


def raiva():
    print('EU TE ODEIO')


teste = seja_educado(raiva)
teste()
---------------------------------------------------

"""


# Decorators com (Syntact Sugar / Açucar Sintático)

def seja_educado_mesmo(funcao):  # Decorator Function
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_mesmo


@seja_educado_mesmo              # Decorator
def apresentando():
    print('Meu nome é Pedro')


apresentando()