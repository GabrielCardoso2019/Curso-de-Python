real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.39
euro = real / 6.38
print('Com R${:.2f} você pode comprar US${:.2f} e EUR{:.2f}'.format(real, dolar, euro))
