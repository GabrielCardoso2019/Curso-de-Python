c = float(input('Informe a temperatura em ºC: '))
f = ((9 * c) / 5) + 32 # <- A ordem de precendencia funciona sem os parenteses
print('A temperatura de {}ºC corresponde a {}ºF'.format(c, f))
