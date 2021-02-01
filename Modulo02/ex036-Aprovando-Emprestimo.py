from time import sleep

casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))

prestacao = casa / (anos * 12)
minimo = salario * 30 / 100

print()
print('PROCESSANDO....')
sleep(3)
print()

print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end=' ')
print('A prestação será de R${:.2f}'.format(prestacao))

print('COMPRANDO tem que pagar R${:.2f} e o mínimo é de R${:.2f}'.format(prestacao, minimo))

if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
