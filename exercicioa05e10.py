# Exercicio 10
# Faça um programa que peça 3 números inteiros e mostre o os tês em ordem decrescente.

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
num3 = int(input('Digite mais um numero: '))

if(num1 > num2):
    if(num1 > num3):
        maior = num1
        if(num2 > num3):
            menor = num3
            meio = num2
        else:
            menor = num2
            meio = num3

if(num3 > num2):
    if(num3 > num1):
        maior = num3
        if(num2 > num1):
            menor = num1
            meio = num2
        else:
            menor = num2
            meio = num1

if (num2 > num1):
    if (num2 > num3):
        maior = num2
        if (num1 > num3):
            menor = num3
            meio = num1
        else:
            menor = num1
            meio = num3

print('Os numeros fornecidos foram {}, {} e {}. A ordem decresente é {} {} {}' .format(num1, num2, num3, maior, meio, menor))