distancia = float(input('Digite a distância percorrida KM'))

if distancia <= 200:
    total = distancia * 0.50
    print(f'O total a se pagar pela viagem é de R${total:.2f}')
else:
    total = distancia * 0.45
    print(f'O total a se pagar pela viagem é de R${total:.2f}')
