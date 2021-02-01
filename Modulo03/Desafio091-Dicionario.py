from operator import itemgetter
from random import randint
from time import sleep

jogo = {'1º Jogador': randint(1, 5),
        '2º Jogador': randint(1, 5),
        '3º Jogador': randint(1, 5),
        '4º Jogador': randint(1, 5)}
ranking = list()

print('\033[1;31m---- VALORES SORTEADOS ----\033[m')
for v, k in jogo.items():
    print(f'    - {v} tirou {k} nos dados.')
    sleep(1)

print('\033[1;31m---- RANKING DOS JOGADORES ----\033[m')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com valor de dado {v[1]}')
    sleep(1)
