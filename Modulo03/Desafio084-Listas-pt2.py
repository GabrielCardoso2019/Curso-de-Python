galera = list()
dados = list()
totalPessoas = 0

while True:
    dados.append(str(input('Digite seu nome: ')))
    dados.append(int(input('Digite seu peso: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    galera.append(dados[:])
    dados.clear()
    totalPessoas += 1
    if resp in 'Nn':
        break

print('===' * 20)
print(f'Você cadastrou {totalPessoas} pessoas')

for p in galera:
    if p[1] <= 70:
        print(f'{p[0]} está na lista dos pesos pesados com {p[1]}Kg')
    elif p[1] > 70:
        print(f'{p[0]} está na lista dos pesos leves com {p[1]}Kg')
