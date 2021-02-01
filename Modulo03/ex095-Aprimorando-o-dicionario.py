from time import sleep

time = list()
jogador = dict()
partidas = list()

while True:
    jogador['NOME'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["NOME"]} jogou ? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c+1}? ')))
    jogador['GOLS'] = partidas[:]
    jogador['TOTAL'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('\033[1;31mERRO! Responda apenas S ou N.\033[m')
    if resp == 'N':
        break
print('-=' * 30)

print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        print('FINALIZANDO O PROGRAMA...')
        sleep(2)
        break
    if busca >= len(time):
        print(f'\033[1;31mERRO! Não existe jogador com código {busca}\033[m')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["NOME"]}:')
        for i, g in enumerate(time[busca]["GOLS"]):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('---' * 20)
print('<< PROGRAMA FINALIZADO >>')
