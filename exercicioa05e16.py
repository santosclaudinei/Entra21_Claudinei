# Exercicio 16
# 
# Crie um programa para uma promoção de um posto de combustivel.
# 
# O programa deve pedir ao usuário quantos litros ele quer abastecer e qual combustivel: álcool, diessel ou gasolina
# 
# A promoção é a seguinte:
#  - Para gasolina: Até 20 litros 0% de desconto e acima de 20 litros 10% de desconto
#  - Para diessel: Até 10 litro 1.5% de desconto e acima de 10 litros 5% de desconto
#  - para álcool: Até 10 litros 5% de desconto e acima de 10 litros 10% de desconto.
#  
# Mostre o combustivel que ele selecionou, o total abastecido e a porcentagem de desconto a ser aplicada.
# 
# Não precisa calcular o valor do combustivel!

qtd_litros = float(input('Digite a quantidade de litros desejada: '))
escolha = input('Digite o combustivel desejado: ')

if(escolha == 'Gasolina'):
    if(qtd_litros <= 20):
        desconto = '0%'
        print('O Combustivel escolhido foi {}, a quantidade solicitada foi {} e a porcentagem de desconto é {}' .format(escolha, qtd_litros, desconto))
    else:
        desconto = '10%'
        print('O Combustivel escolhido foi {}, a quantidade solicitada foi {} e a porcentagem de desconto é {}' .format(escolha, qtd_litros, desconto))

if(escolha == 'Alcool'):
    if(qtd_litros <= 10):
        desconto = '1.5%'
        print('O Combustivel escolhido foi {}, a quantidade solicitada foi {} e a porcentagem de desconto é {}' .format(escolha, qtd_litros, desconto))
    else:
        desconto = '5%'
        print('O Combustivel escolhido foi {}, a quantidade solicitada foi {} e a porcentagem de desconto é {}' .format(escolha, qtd_litros, desconto))

if(escolha == 'Diesel'):
    if(qtd_litros <= 10):
        desconto = '5%'
        print('O Combustivel escolhido foi {}, a quantidade solicitada foi {} e a porcentagem de desconto é {}' .format(escolha, qtd_litros, desconto))
    else:
        desconto = '10%'
        print('O Combustivel escolhido foi {}, a quantidade solicitada foi {} e a porcentagem de desconto é {}' .format(escolha, qtd_litros, desconto))