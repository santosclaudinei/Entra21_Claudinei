# Exercicio 1
# 
# Faça um programa que peça 2 numeros inteiros e mostre o maior deles.

num1  = int(input('Digite um numero: '))
num2  = int(input('Digite outro numero: '))
if num1 > num2:
    maior = num1
else:
    maior = num2
print('O maior entre os dois numeros foi {}' .format(maior))