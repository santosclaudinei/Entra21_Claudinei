# Execicios 03 - Escreva um programa que contenha um menu com 4 opções:

'''A) soma
B) média
C) divisão
D) Sair

As opções podem ser escolhidas com as letras maiusculas ou minusculas.

Para a opção soma, deve solicitar 2 números, fazer a soma e mostrar o resultado.

Para a opção média, deve solicitar 4 números, fazer a média e mostrar os resultados.

Para a opção divisão, deve solicitar 2 números, dividir o primeiro pelo segundo e montrar o resultado. Caso o segundo for igual a 0, então deve mostrar o a mensagem "Erro! Não pode dividir por ZERO!"

Para a opção sair, deve aparecer a mensagem: "Muito Obrigado e Volte sempre!'''

print('''
############################### CALCULADORA INTERATIVA #########################################

A) SOMA
B) MÉDIA
C) DIVISÃO
D) SAIR

''')

opcao = input('Digite a opção desejada com base no menu: ')

if(opcao == 'A') or (opcao == 'a'):
    n1 = float(input('Digite um numero: '))
    n2 = float(input('Digite outro numero: '))
    soma = n1 + n2
    print('A opção escolhida foi a SOMA e os numeros fornecidos foram {} e {}. O resultado do somatório foi {}' .format(n1, n2, soma))
elif(opcao == 'B') or (opcao == 'b'):
    n1 = float(input('Digite um numero: '))
    n2 = float(input('Digite outro numero: '))
    media = (n1 + n2) / 2
    print('A opção escolhida foi a MÉDIA e os numeros fornecidos foram {} e {}. O resultado do somatório foi {}' .format(n1, n2, media))
elif(opcao == 'C') or (opcao == 'c'):
    n1 = float(input('Digite um numero: '))
    n2 = float(input('Digite outro numero: '))
    divisao = n1 + n2
    print('A opção escolhida foi a SOMA e os numeros fornecidos foram {} e {}. O resultado do somatório foi {}' .format(n1, n2, divisao))
elif(opcao == 'd') or (opcao == 'D'):
        print('Você escolheu a opção SAIR! Obrigado por utilizar o nosso sistema.')