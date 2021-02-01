campeonato = dict()
gols = list()

campeonato['NOME'] = str(input('Nome do Jogador: '))
part = int(input(f'Quantas partidas {campeonato["NOME"]} jogou? '))
campeonato['PARTIDAS'] = part
for c in range(part):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
    campeonato['GOLS'] = gols[:]
    campeonato['TOTAL'] = sum(gols)
print('-=' * 30)
print(campeonato)
print('-=' * 30)

for v, k in campeonato.items():
    print(f'O campo \033[1m{v}\033[m tem o valor {k}.')
print('-=' * 30)

print(f'O jogador {campeonato["NOME"]} jogou {campeonato["PARTIDAS"]} partidas')
somaGols = sum(gols)
for i, v in enumerate(campeonato['GOLS']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {somaGols} gols')
