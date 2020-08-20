# Exercicio 15
# Crie um programa que peça ao usuário que digite um número de 1 a 12 e mostre o mês correspondente ao número.

numero = int(input('Digite um numero entre 1 e 12: '))

if ((numero >= 1) or (numero <= 12)):
    if (numero == 1):
        print('O numero digitado foi {}. ele corresponde à JANEIRO!' .format(numero))
    if (numero == 2):
        print('O numero digitado foi {}. ele corresponde à FEVEREIRO!' .format(numero))
    if (numero == 3):
        print('O numero digitado foi {}. ele corresponde à MARÇO!' .format(numero))
    if (numero == 4):
        print('O numero digitado foi {}. ele corresponde à ABRIL!' .format(numero))
    if (numero == 5):
        print('O numero digitado foi {}. ele corresponde à MAIO!' .format(numero))
    if (numero == 6):
        print('O numero digitado foi {}. ele corresponde ao JUNHO!' .format(numero))
    if (numero == 7):
        print('O numero digitado foi {}. ele corresponde ao JULHO!' .format(numero))
    if (numero == 8):
        print('O numero digitado foi {}. ele corresponde ao AGOSTO!' .format(numero))
    if (numero == 9):
        print('O numero digitado foi {}. ele corresponde ao SETEMBRO!' .format(numero))
    if (numero == 10):
        print('O numero digitado foi {}. ele corresponde ao OUTUBRO!' .format(numero))
    if (numero == 11):
        print('O numero digitado foi {}. ele corresponde ao NOVEMBRO!' .format(numero))
    if (numero == 12):
        print('O numero digitado foi {}. ele corresponde ao DEZEMBRO!' .format(numero))