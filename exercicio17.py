# Exercicio 17
# A formula de calculo de área de um circulo é:
# 
# area = pi*r²
# 
# Sabemos que:
# 
# pi = 3.14
# r = raio da circunferência em metros (float)
# 
# Crie um programa que peça ao usuário o raio e calcule a área da circunferência
# 
raio = float(input('Digite o raio que deseja calcular a area do circulo: '))
pi = 3.14
area = (pi * (raio ** 2))
print('O raio para base de calculo é {} e a area resultante é {}' .format(raio, area))