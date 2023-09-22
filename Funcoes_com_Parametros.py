"""
Funções com Parâmetro (de entrada)

- Funções que recebem dados para serem processados dentro da mesma


#Refatorando
#Nenhuma entrada e mesmo processamento

def quadrado_de_7():
    return 7 * 7
----------------------------------------------


# Parâmetros são variáveis declaradas na definição de uma função
# Argumentos são dados passados durante a execução de uma funçãp
#
def nome_completo(nome, sobrenome):
    return 'Seu nome completo é 'nome, sobrenome

# Quando utilizamos os nomes dos parâmetros para informá-los, podemos utilizar qualquer ordem.
print(nome_completo(sobrenome='Marques', nome='Alves'))
"""


#Recebe um parâmetro (num) e ele é obrigatório
def quadrado(num):
    return num * num

print(quadrado(2))
print(quadrado(10))
print(quadrado(5))