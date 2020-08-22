# Execicios 04 - Exercicio retirado do site <https://wiki.python.org.br/EstruturaDeDecisao>
# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

ladoA = int(input('Digite o valor para o lado A do triangulo: '))
ladoB = int(input('Digite o valor para o lado B do triangulo: '))
ladoC = int(input('Digite o valor para o lado C do triangulo: '))

if((ladoA + ladoB > ladoC) and (ladoA + ladoC > ladoB) and (ladoB + ladoC > ladoA)):
    print('Satisfaz as condições para ser um triangulo!')
else:
    print('Não Satisfaz as condições para ser um triangulo!')
if (ladoA == ladoB) and (ladoA == ladoC) and (ladoB == ladoC):
    print('As medidas informadas foram {}, {} e {} e o triangulo resultante foi EQUILÁTERO!' .format(ladoA, ladoB, ladoC))

elif(ladoA == ladoB) and (ladoA == ladoC) and (ladoB != ladoC):
    print('As medidas informadas foram {}, {} e {} e o triangulo resultante foi ISÓCELES!' .format(ladoA, ladoB, ladoC))

elif(ladoA != ladoB) and (ladoA == ladoC) and (ladoB == ladoC):
    print('As medidas informadas foram {}, {} e {} e o triangulo resultante foi ISÓCELES!' .format(ladoA, ladoB, ladoC))

elif(ladoA == ladoB) and (ladoA != ladoC) and (ladoB == ladoC):
    print('As medidas informadas foram {}, {} e {} e o triangulo resultante foi ISÓCELES!' .format(ladoA, ladoB, ladoC))

elif(ladoA != ladoB) and (ladoA != ladoC) and (ladoB !=ladoC):
    print('As medidas informadas foram {}, {} e {} e o triangulo resultante foi ESCALENO!' .format(ladoA, ladoB, ladoC))