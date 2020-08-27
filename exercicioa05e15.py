# Exercicio 15
# Crie um programa que peça ao usuário que digite um número de 1 a 12 e mostre o mês correspondente ao número.

numero = int(input('Digite um numero entre 1 e 12: '))

if ((numero >= 1) or (numero <= 12)):
    if (numero == 1):
        print('O numero digitado foi {}. ele corresponde à JANEIRO!' .format(numero))
    elif (numero == 2):
        print('O numero digitado foi {}. ele corresponde à FEVEREIRO!' .format(numero))
    elif (numero == 3):
        print('O numero digitado foi {}. ele corresponde à MARÇO!' .format(numero))
    elif (numero == 4):
        print('O numero digitado foi {}. ele corresponde à ABRIL!' .format(numero))
    elif (numero == 5):
        print('O numero digitado foi {}. ele corresponde à MAIO!' .format(numero))
    elif (numero == 6):
        print('O numero digitado foi {}. ele corresponde ao JUNHO!' .format(numero))
    elif (numero == 7):
        print('O numero digitado foi {}. ele corresponde ao JULHO!' .format(numero))
    elif (numero == 8):
        print('O numero digitado foi {}. ele corresponde ao AGOSTO!' .format(numero))
    elif (numero == 9):
        print('O numero digitado foi {}. ele corresponde ao SETEMBRO!' .format(numero))
    elif (numero == 10):
        print('O numero digitado foi {}. ele corresponde ao OUTUBRO!' .format(numero))
    elif (numero == 11):
        print('O numero digitado foi {}. ele corresponde ao NOVEMBRO!' .format(numero))
    elif (numero == 12):
        print('O numero digitado foi {}. ele corresponde ao DEZEMBRO!' .format(numero))