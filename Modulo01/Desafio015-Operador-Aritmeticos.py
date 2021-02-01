km = float(input('Digite a quantidade de Km percorridos com o carro: '))
qtdDias = int(input('Digite a quantidade de dias utilizados: '))
pago = (qtdDias * 60) + (km * 0.15)

print('O total a pagar é de R${:.2f}'.format(pago))
