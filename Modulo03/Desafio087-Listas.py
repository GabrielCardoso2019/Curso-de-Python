matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = somacolum = 0

# Estrutura para alimentação da matriz
for line in range(0, 3):
    for colum in range(0, 3):
        matriz[line][colum] = int(input(f'Digite um valor para [{line}, {colum}]: '))
print('-=' * 30)

# Estrutura para apresentação na tela
for line in range(0, 3):
    for colum in range(0, 3):
        print(f'[{matriz[line][colum]:^5}]', end='')
        # Faz a soma de todos os números pares da matriz
        if matriz[line][colum] % 2 == 0:
            spar += matriz[line][colum]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é: {spar}')

# Soma dos valores da terceira coluna da matriz
for line in range(0, 3):
    somacolum += matriz[line][2]
print(f'A soma dos valores da terceira coluna é: {somacolum}')

# Soma dos valores na segunda linha
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}')

