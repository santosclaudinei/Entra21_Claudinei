# 3) Estas 3 listas:
# Estas listas são referente as vendas dos vendedores Armando, Paulo e Eduardo.
# 
# 3.1) Com base nelas e usando funções da lista mostradas em aula, mostre:
# A média de vendas de cada um;
# A venda total de cada vendedor;
# A quantidade de vendas de cada vendedor.
# 
# 3.2) Calcule o valor de comissão que o dono da loja deve pagar para seus funcionários seguindo a regra:
# 
# Para total de vendas de 0.00 a 1000.00 Reais - 1%
# Para total de vendas de 1000.01 a 2500.00 Reais - 1.5%
# Para total de vendas de 2500.01 a 5000.00 Reais - 2%
# Para total de vendas a cima de 5000.01 Reais - 3%

vendas_armando = [100.00, 500.00, 258.50, 710.00, 50.50, 750.00]                        # Lista contem as vendas feitas
vendas_eduardo = [10.00, 1050.00, 859.75, 199.05, 500.50,750.00, 568.60, 950.00 ]
vendas_paulo = [950.00, 89.90, 2500.00, 1750.00,500.00]

total_armando = sum(vendas_armando)                                                     # Faz a soma dos valores da lista
num_vendas_armando = len(vendas_armando)                                                # Retorna o numero de elementos
media_armando = total_armando / num_vendas_armando                                      # Calcula valor medio de vendas 

total_eduardo = sum(vendas_eduardo)
num_vendas_eduardo = len(vendas_eduardo)
media_eduardo = total_eduardo / num_vendas_eduardo

total_paulo = sum(vendas_paulo)
num_vendas_paulo = len(vendas_paulo)
media_paulo = total_paulo / num_vendas_paulo

print(f'A média de vendas efetuadas por Armando foi R$ {media_armando:.2f}')            # Imprime a media de vendas
print(f'O valor total de vendas de Armando foi R$ {total_armando}')                     # Imprime o total de vendas
print(f'O numero de vendas efetuadas por Armando foi {num_vendas_armando}')             # Imprime numero de vendas
print(f'\nA média de vendas efetuadas por Eduardo foi R$ {media_eduardo:.2f}')
print(f'O valor total de vendas de Eduardo foi R$ {total_eduardo}')
print(f'O numero de vendas efetuadas por Eduardo foi {num_vendas_eduardo}')
print(f'\nA média de vendas efetuadas por Paulo foi R$ {media_paulo:.2f}')
print(f'O valor total de vendas de Paulo foi R$ {total_paulo}')
print(f'O numero de vendas efetuadas por Paulo foi {num_vendas_paulo}\n')

# 3.2) Calcule o valor de comissão que o dono da loja deve pagar para seus funcionários seguindo a regra:
# 
# Para total de vendas de 0.00 a 1000.00 Reais - 1%
# Para total de vendas de 1000.01 a 2500.00 Reais - 1.5%
# Para total de vendas de 2500.01 a 5000.00 Reais - 2%
# Para total de vendas a cima de 5000.01 Reais - 3%

if(total_armando > 0) and (total_armando <= 1000):                                      # Condições verificam comissão
    comissao_armando = total_armando * (1 / 100)
    print(f'A comissão a ser recebida por Armando é R$ {comissao_armando:.2f}')
elif(total_armando > 1000) and (total_armando <= 2500):
    comissao_armando = total_armando * (1.5 / 100)
    print(f'A comissão a ser recebida por Armando é R$ {comissao_armando:.2f}')
elif(total_armando > 2500) and (total_armando <= 5000):
    comissao_armando = total_armando * (2 / 100)
    print(f'A comissão a ser recebida por Armando é R$ {comissao_armando:.2f}')
elif(total_armando > 5000.0):
    comissao_armando = total_armando * (3 / 100)
    print(f'A comissão a ser recebida por Armando é R$ {comissao_armando:.2f}')

if(total_eduardo > 0) and (total_eduardo <= 1000):                                      # Condições verificam comissão
    comissao_eduardo = total_eduardo * (1 / 100)
    print(f'A comissão a ser recebida por Eduardo é R$ {comissao_eduardo:.2f}')
elif(total_eduardo > 1000) and (total_eduardo <= 2500):
    comissao_eduardo = total_eduardo * (1.5 / 100)
    print(f'A comissão a ser recebida por Eduardo é R$ {comissao_eduardo:.2f}')
elif(total_eduardo > 2500) and (total_eduardo <= 5000):
    comissao_eduardo = total_eduardo * (2 / 100)
    print(f'A comissão a ser recebida por Eduardo é R$ {comissao_eduardo:.2f}')
elif(total_eduardo > 5000.0):
    comissao_eduardo = total_eduardo * (3 / 100)
    print(f'A comissão a ser recebida por Eduardo é R$ {comissao_eduardo:.2f}')

if(total_paulo > 0) and (total_paulo <= 1000):                                          # Condições verificam comissão
    comissao_paulo = total_paulo * (1 / 100)
    print(f'A comissão a ser recebida por Paulo é R$ {comissao_paulo:.2f}')
elif(total_paulo > 1000) and (total_paulo <= 2500):
    comissao_paulo = total_paulo * (1.5 / 100)
    print(f'A comissão a ser recebida por Paulo é R$ {comissao_paulo:.2f}')
elif(total_paulo > 2500) and (total_paulo <= 5000):
    comissao_paulo = total_paulo * (2 / 100)
    print(f'A comissão a ser recebida por Paulo é R$ {comissao_paulo:.2f}')
elif(total_paulo > 5000.0):
    comissao_paulo = total_paulo * (3 / 100)
    print(f'A comissão a ser recebida por Paulo é R$ {comissao_paulo:.2f}')