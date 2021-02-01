from random import randint

numUser = int(input('Adivinhe o número que a máquina pensou: '))
numMaquina = randint(1, 5)

if numUser == numMaquina:
    print('PARABÉNS VOCÊ ACERTOU E VENCEU A MÁQUINA! A MÁQUINA ESCOLHEU O NÚMERO {}'.format(numMaquina))
else:
    print('VOCÊ ERROU A MÁQUINA VENCEU!')
