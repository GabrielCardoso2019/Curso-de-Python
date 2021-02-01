altura = float(input('Altura da parede em M: '))
largura = float(input('Largura da parede em M: '))

comprimento = altura * largura
tinta = comprimento / 2
print('A quantidade de tinta necessária para pintar essa parede é de {}L'.format(tinta))
