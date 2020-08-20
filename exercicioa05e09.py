# Exercicio 9
# Faça um programa que peça 3 números inteiros e mostre o os tês em ordem crescente.

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
num3 = int(input('Digite mais um numero: '))

if((num1 > num2) & (num1 > num3)):
    if num2 > num3:
        maior = num1
        meio = num2
        menor = num3
    if num3 > num2:
        maior = num1
        meio = num3
        menor = num2
if((num2 > num1) & (num2 > num3)):        
    if num1 > num3:
        maior = num2
        meio = num1
        menor = num3
    if num1 < num3:
        maior = num2
        meio = num3
        menor = num1
if((num3 > num1) & (num3 > num2)):       
    if num1 > num2:
        maior = num3
        meio = num1
        menor = num2
    if num1 < num2:
        maior = num3
        meio = num2
        menor = num1

print('O Maior numero é:', maior)
print('O Numero do meio é', meio)
print('O Menor numero é:', menor)