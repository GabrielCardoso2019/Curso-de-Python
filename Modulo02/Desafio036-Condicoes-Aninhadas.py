"""
Calcule o valor da prestação mensal, sabendo que ela não
pode exceder 30% do salário ou então o emprestimo será negado.
"""

from time import sleep

print('-=-' * 20)
print('\033[1;31;40mEMPRÉSTIMO BANCÁRIO\033[m')
print('-=-' * 20)

nomeComprador = str(input('Informe seu nome: '))
valorCasa = float(input('Informe o valor da casa: R$'))
salarioComprador = float(input('Informe seu salário: R$'))
anosPagamento = int(input('Informe em quantos anos pagára a casa: '))

prestacao = valorCasa / (anosPagamento * 12)
minimo = salarioComprador * 30 / 100

print()
print('PROCESSANDO...')
sleep(3)
print()

print('Para pagar uma casa de R${:.2f} em {} anos'.format(valorCasa, anosPagamento), end=' ')
print('A prestação será de R${:.2f}'.format(prestacao))

print('COMPRANDO tem que pagar {:.2f} e o mínimo é de {:.2f}'.format(prestacao, minimo))

if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')

