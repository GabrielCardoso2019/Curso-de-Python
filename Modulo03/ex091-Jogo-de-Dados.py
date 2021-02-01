from random import randint
from time import sleep
from operator import itemgetter

jogo = {'1º Jogador': randint(1, 6),
        '2º Jogador': randint(1, 6),
        '3º Jogador': randint(1, 6),
        '4º Jogador': randint(1, 6)}

ranking = list()
print('\033[1;31m---- VALORES SORTEADOS ----\033[m')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

print('\033[1;31m---- RANKING DOS JOGADORES ----\033[m')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'    {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
