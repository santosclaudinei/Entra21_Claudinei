# Exercicio 12
# 
# Crie um program que peça ao usuário que digite 2 números reias(float) e mostre:
# 
# A soma dos dois
# A multiplicação dos dois
# A divisão do primeiro com o segundo
# A subtração dos dois

num1 = float(input('Digite o primeiro numero:'))
num2 = float(input('Digite o segundo numero:'))

soma = num1 + num2
multiplicacao = num1 * num2
divisao = num1 / num2
subtracao = num1 - num2

print('A soma de {} e {} é'.format(num1,num2), soma)
print('A soma de {} e {} é'.format(num1,num2), multiplicacao)
print('A soma de {} e {} é'.format(num1,num2), divisao)
print('A soma de {} e {} é'.format(num1,num2), subtracao)
