# Exercicio 12
# 
# Crie um programa que peça 2 números.
# 
# Depois mostre um menu interativo contendo 5 operações matemáticas do python
# (adição, subtração, multiplicação, divisão e expoente)
# 
# Peça para o usuário escolher uma destas opções e mostre o resultado da operação escolhida.

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))

print('''
########################################## CALCULADORA INTERATIVA ############################################

ESCOLHA UMA DAS OPÇÕES ABAIXO:

1 - SOMA
2 - SUBTRAÇÃO
3 - MULTIPLICAÇÃO
4 - DIVISÃO
5 - EXPONENCIAÇÃO

##############################################################################################################
''')
escolha = int(input('Digite a opção desejada: '))

if (escolha == 1):
    res = num1 + num2
elif (escolha == 2):
    res = num1 - num2
elif (escolha == 3):
    res = num1 * num2
elif (escolha == 4):
    res = num1 / num2
elif (escolha == 5):
    res = num1 ** num2

print('Diante das escolhas {} e {} o resultado da operação foi {} ' .format(num1, num2, res))
