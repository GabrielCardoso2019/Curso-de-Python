distancia = int(input('Digite a distância percorrida: '))
if distancia <= 200:
    print('Você pagará R${:.2f} pela viagem'.format(distancia * 0.50))
else:
    print('Você pagará R${:.2f} pela viagem'.format(distancia * 0.45))
