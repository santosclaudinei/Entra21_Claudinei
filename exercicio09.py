
# Exercicio 9
# Faça um programa que peça o nome do cliente, a quantidade do produto (inteiro) e o preço (float).
# 
# Mostre o nome do cliente e o valor total da venda.


nome = input("Digite seu nome: ")
qtd = int(input("Digite a quantidade desejada: "))
preco = float(input("Digite o preço do produto: "))
valorTotal= qtd * preco
print(nome, "O valor total da sua compra é: R$", valorTotal)