# Exercicio 6
# Escreva um programa que peça 2 números e mostre eles em ordem crescente

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))

if num1 > num2:
    menor = num2
if num2 > num1:
    menor = num1
print('O menor numero entre {} e {} é {}' .format(num1, num2, menor))