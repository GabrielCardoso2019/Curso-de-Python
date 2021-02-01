velocidade = int(input('Digite a velocidade do carro: '))

if velocidade > 80:
    print('Você foi multado por execesso de velocidade!')
    print('Sua multa é de R${:.2f} são R$7,00 a cada KM ultrapassado do limite'.format((velocidade - 80) * 7))
elif velocidade == 80:
    print('Você está no limite de velocidade, diminua ou será multado')
else:
    print('Tenha uma ótima viagem e dirija com cuidado')
