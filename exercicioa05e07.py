# Exercicio 7
# Faça um programa que peça 3 números inteiros e mostre o menor número.

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
num3 = int(input('Digite mais um numero: '))

if ((num1 > num2) and (num1 > num3) and (num2 > num3)):
    menor = num3
elif num3 > num2:
    menor = num2
    if ((num2 > num1) and (num2 > num3) and (num1 > num3)):
        menor = num3
    elif num3 > num1:
        menor = num1
        if ((num3 > num2) and (num3 > num1) and (num2 > num1)):
            menor = num1
        elif num1 > num2:
            menor = num2
print('Você digitou 1º o {}, 2º o {} e 3º o {} e o menor numero é {}: ' .format(num1, num2, num3, menor))



