from time import sleep
from random import randint

def sorteia(lista):
    print('\033[1;34mSORTEANDO 5 NÚMEROS DA LISTA: \033[m', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(randint(1, 10))
        print(f'\033[1m{n}\033[m ', end='', flush=True)
        sleep(0.3)
    print('\033[1;34mPRONTO!\033[m')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'\033[1;34mSOMANDO OS VALORES PARES DE\033[m \033[1m{lista}\033[m, \033[1;34mTEMOS\033[m \033[1;m{soma}\033[m')

num = list()
sorteia(num)
somaPar(num)
