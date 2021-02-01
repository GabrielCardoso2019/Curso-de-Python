def ficha(nome='<Desconhecido>', gols=0):
    """
    --> Mostra gols e nome de jogador
    :param nome: nome do jogador
    :param gols: quantidade de gols feitos
    :return: nome e gols do jogador
    """
    print('-=' * 20)
    print(f'O jogador {nome} fez {gols} gol(s) na partida.')

# Programa Principal
n = str(input('Digite o nome do Jogador: '))
g = str(input(f'Digite o número de gols do(a) {n}: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)

