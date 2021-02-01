from time import sleep

velo = int(input('Digite a velocidade do carro: '))
multa = (velo - 80) * 7

if velo > 80:
    print('Você está acima do limite!')
    print(f'Você recebeu uma multa de R${multa}. Tenha mais cuidado.')
elif velo == 80:
    print('Diminua a velocidade.Você está quase no limite da via')
else:
    print('Você está dentro do limite. Ótima viagem!')
