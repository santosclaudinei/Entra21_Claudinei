# Execicios 01 - Escreva um programa que calcule a porcentagem de comissão de vendedores com as seguintes condições
# Venda Total
# de R$ 0.00 a R$ 30000.00 - 0%
# de R$ 30000.01 a R$ 50000.00 - 1.5%
# de R$ 50000.01 a R$ 100000.00 - 2.5%
# Acima de R$ 100000.00 - 3.5%

venda_total = float(input('Digite o valor da sua venda total: '))                                               #Recebe entrada de dados através do teclado

if(venda_total >= 0) and (venda_total <= 3000.0):                                                               #
    porcentagem = (venda_total * (0/100))
    print('A venda total é R${} e a porcentagem de comissão é R${:.2f}' .format(venda_total, porcentagem))
if(venda_total > 3000.0) and (venda_total <= 5000.0):
    porcentagem = (venda_total * (1.5/100))
    print('A venda total é R${} e a porcentagem de comissão é R${:.2f}' .format(venda_total, porcentagem))
if(venda_total > 5000.0) and (venda_total <= 10000.0):
    porcentagem = (venda_total * (2.5/100))
    print('A venda total é R${} e a porcentagem de comissão é R${:.2f}' .format(venda_total, porcentagem))
if(venda_total > 10000.0):
    porcentagem = (venda_total * (3.5/100)) 
    print('A venda total é R${} e a porcentagem de comissão é R${:.2f}' .format(venda_total, porcentagem))
