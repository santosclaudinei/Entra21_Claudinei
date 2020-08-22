# Execicios 02 - Escreva um programa que receba 4 notas e calcule a média. Mostre a seguinte mensagem conforme a 
# media final.

# Media Final
# de 0 a 5 - Reprovado
# de 5 a 6.5 - Recuperação
# de 6.5 a 9 - Aprovado
# Acima de 9 - Aprovado com louvor

nota1 = float(input('Digita a sua primeira nota: '))
nota2 = float(input('Digita a sua segunda nota: '))
nota3 = float(input('Digita a sua terceira nota: '))
nota4 = float(input('Digita a sua quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4) / 4

if (media >= 0.0) and (media < 5.0):
    print('sua média foi {}. por esse motivo voce esta REPROVADO!!!' .format(media))
if (media >= 5.0) and (media <6.5):
    print('sua média foi {}. por esse motivo voce esta na RECUPERAÇÃO!!!' .format(media))
if (media >= 6.5) and (media < 9.0):
    print('sua média foi {}. por esse motivo voce esta APROVADO!!!' .format(media))
if (media > 9.0):
    print('sua média foi {}. por esse motivo voce esta APROVADO COM LOUVOR!!!' .format(media))