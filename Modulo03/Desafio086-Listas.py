matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Estrutura para alimentação da matriz
for line in range(0, 3):
    for colum in range(0, 3):
        matriz[line][colum] = int(input(f'Digite um valor para [{line}, {colum}]: '))
print('-=' * 30)

# Estrutura para apresentação na tela
for line in range(0, 3):
    for colum in range(0, 3):
        print(f'[{matriz[line][colum]:^5}]', end='')
    print()
