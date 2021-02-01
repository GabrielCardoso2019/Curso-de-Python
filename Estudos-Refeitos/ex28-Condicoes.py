from random import randint
from time import sleep

comp = randint(1, 6)
numUser = int(input('Tente adivinhar o número que a máquina pensou: '))

if numUser == comp:
    sleep(1)
    print(f'USUÁRIO VENCEU! Você acertou. O número da máquina foi {comp}')
else:
    sleep(1)
    print(f'MÁQUINA VENCEU! A máquina pensou no número {comp}')
