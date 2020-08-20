# Exercicio 14
# Crie um programa que peça ao usuário digitar um número de 1 a 7 e mostre o dia da semana correspondente sendo que segunda feira é o numero 1 e domingo é 7.

numero = int(input('Digite um numero entre 1 e 7: '))

if ((numero >= 1) or (numero <= 7)):
    if (numero == 1):
        print('O numero digitado foi {}. ele corresponde à SENGUNDA-FEIRA!' .format(numero))
    if (numero == 2):
        print('O numero digitado foi {}. ele corresponde à TERÇA-FEIRA!' .format(numero))
    if (numero == 3):
        print('O numero digitado foi {}. ele corresponde à QUARTA-FEIRA!' .format(numero))
    if (numero == 4):
        print('O numero digitado foi {}. ele corresponde à QUINTA-FEIRA!' .format(numero))
    if (numero == 5):
        print('O numero digitado foi {}. ele corresponde à SEXTA-FEIRA!' .format(numero))
    if (numero == 6):
        print('O numero digitado foi {}. ele corresponde ao SABADO!' .format(numero))
    if (numero == 7):
        print('O numero digitado foi {}. ele corresponde ao DOMINGO!' .format(numero))