# Exercicio 5
# Faça um programa que peça uma senha ao usuário.
# 
# Se a senha for igual a "Abacaxi" deve aparecer a mensagem "Entrada liberada"
# 
# Caso contrário deve aparecer a mensagem "Senha incorreta"

senha = input('Digite sua senha: ')

if senha == 'Abacaxi':
    print('ENTRADA LIBERADA!!!')
else:
    print('SENHA INCORRETA!!!')