# Exercicio 13
# 
# Crie um programa que peça o nome do cliente, idade, endereço, email e telefone.
# 
# Depois crie um menu interativo com as seguintes opções: Dados, Endereço, Contato.
# 
# Se o usuário selecionar "Dados" deve aparecer o nome do cliente e a idade
# 
# Se o usuário selecionar "Endereço" deve aparecer o nome do cliente e o endereço
# 
# Se o usuário selecionar "Contato" deve aparecer o nome do cliente, email e o telefone

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
endereco = input('Digite seu endereço: ')
email = input('Digite seu endereço de email: ')
telefone = input('Digite seu numero de telefone: ')

print('''
###################################### SISTEMA DE CADASTRO INTERATIVO #########################################

ESCOLHA UMA DAS OPÇÕES ABAIXO:

1 - DADOS
2 - ENDEREÇO
3 - CONTATO

##############################################################################################################
''')

escolha = int(input('Digite a opção desejada: '))

if(escolha == 1):
    print('Nome do Cliente: ', nome, end ='  ')
    print('Idade do Cliente: ', idade)
elif(escolha == 2):
    print('Nome do Cliente: ', nome, end ='  ')
    print('Endereço do Cliente: ', endereco)
elif(escolha == 3):
    print('Nome do Cliente: ', nome, end ='  ')
    print('Email do Cliente: ', email)
    print('Telefone do Cliente: ', telefone)