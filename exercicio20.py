#  Exercicio 20
# Usando a seguinte fórmula:
# 
# valor_receber = dinheiro_emprestado*(1+(taxa_juros/100))**tempo_emprestimo
# 
# Crie um programa que solicite ao usuário o valor do dinheiro emprestado, 
# a taxa de juros em porcentagem e o tempo do empréstimo.
# 
# Mostre na telas o valor do dinheiro emprestado, a taxa de juros em porcentagem, 
# tempo do empréstimo e o valor que deve ser devolvido no final do empréstimo.

dinheiro_emprestado = float(input('Informe o dinheiro que você esta emprestando: '))
tempo_emprestimo = int(input('Digite a quantidade de tempo solicitado para pagamento do emprestimo: '))
taxa_juros = float(input('Digite a taxa de juros atual: '))
valor_receber = dinheiro_emprestado*(1+(taxa_juros/100))**tempo_emprestimo

print('O valor emprestado é {} por {} meses a uma taxa de juros de {}%. resultando numa devolução de {}' .format(dinheiro_emprestado, tempo_emprestimo, taxa_juros, valor_receber))
