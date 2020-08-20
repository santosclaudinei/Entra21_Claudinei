# Exercicio 8
# Faça um programa que peça 3 números inteiros e mostre o número maior.

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
num3 = int(input('Digite mais um numero: '))

if(num1 > num2):
    if(num1 > num3):
        maior = num1
if(num2 > num1):
    if(num2 > num3):
        maior = num2
if(num3 > num1):
    if(num3 > num2):
        maior = num3
print('O maior numero entre {}, {} e {} é: {}' .format(num1, num2, num3, maior))





