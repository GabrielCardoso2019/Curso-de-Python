from random import randint

computador = randint(0, 11)
jogador = ''
palpites = 0

while computador != jogador:
    jogador = int(input('Digite um número: '))
    palpites += 1
    if jogador == computador:
        print('Jogador venceu!')
    else:
        print('Computador venceu')
print(f'Você deu {palpites} palpites e venceu!!')
