# Exercicio 10
# Faça um programa que peça o nome de 2 produtos, a quantidade comprada de cada produto (inteiro) 
# e o valor (float) de cada um.
# 
# Mostre o nome a quantidade, preço por unidade e o total de cada produto.

produto1 = input("Digite o nome do primeiro produto: ")
produto2 = input("Digite o nome do segundo produto: ")
qtd_produto1 = int(input("Digite a quantidade desejada do primeiro produto: "))
qtd_produto2 = int(input("Digite a quantidade desejada do segundo produto: "))
valor_produto1 = float(input("Digite o valor do primeiro produto: "))
valor_produto2 = float(input("Digite o valor do segundo produto: "))
valor_total1 = qtd_produto1 * valor_produto1
valor_total2 = qtd_produto2 * valor_produto2


print('Foi comprado',qtd_produto1,'unidades de',produto1,'\nO valor da unidade é: R$', valor_produto1,'\nE o total a ser pago é de: R$', valor_total1)
print('\nFoi comprado',qtd_produto2,'unidades de',produto2,'\nO valor da unidade é: R$', valor_produto2,'\nE o total a ser pago é de: R$', valor_total2)