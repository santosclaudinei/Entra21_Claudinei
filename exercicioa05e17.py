# Exercicio 17
# crie um programa que peça 4 notas de um aluno e calcule a média "(nota1+nota2+nota3+nota4)/4" e retorne:
# 
# Pra média igual a 10 apareça a mensagem "Aprovado com louvor"
# Pra média maior igual a 7 apareça a mensagem "Aprovado"
# Pra média menor que 7 apareça a mensagem "Reprovado"

nota1 = float(input('Digite a nota da primeira unidade: '))
nota2 = float(input('Digite a nota da segunda unidade: '))
nota3 = float(input('Digite a nota da terceira unidade: '))
nota4 = float(input('Digite a nota da quarta unidade: '))
media = ((nota1 + nota2 + nota3 + nota4) / 4)

if (media < 7.0):
    print('Reprovado!')
if (10.0 > media >= 7.0 ):
        print('Aprovado!')
if (media == 10.0):
    print('Aprovado com louvor!')
    