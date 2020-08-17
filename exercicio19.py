# Exercicio 19
# Para calcular o valor do empréstimo usa-se a seguinte fórmula:

# valor_receber = dinheiro_emprestado*(1+(taxa_juros/100))**tempo_emprestimo

# Sendo que:
# valor_receber (float) -> É o valor que você deve receber de volta. Este valor é sempre maior que o valor 
# emprestado.
# dinheiro_emprestado (float) -> É o valor que você está emprestando.
# taxa_juros (float) -> Essa é a taxa de juros em porcentagem que irá ser aplicado no valor emprestado todo 
# o mês aumentando o valor a receber
# tempo_emprestimo (inteiro) -> É o tempo que vai demorar para voê receber o dinheiro de volta.

# Se você emprestou R$150.00 por 3 mêses a uma taxa de 4.5 porcento ao mês, você deve fazer a seguinte conta:

# valor_receber = 150*(1+(4.5/100))**3

# o resultado deve ser: 171.17491874999996

# Crie um programa que calcule o emprestimo de R$250.00 a uma taxa de 5.5 porcento ao mês. 
# O programa deve pedir ao usuário que digite quantos mêses deve durar o empréstimo e mostre na tela o valor a ser recebido.


dinheiro_emprestado = float(250)
tempo_emprestimo = int(input('Digite a quantidade de tempo solicitado para pagamento do emprestimo: '))
taxa_juros = float(5.5)
valor_receber = dinheiro_emprestado*(1+(taxa_juros/100))**tempo_emprestimo

print('O valor emprestado é R${} por {} meses a uma taxa de juros de {} %. resultando numa devolução de {}' .format(dinheiro_emprestado, tempo_emprestimo, taxa_juros, valor_receber))
