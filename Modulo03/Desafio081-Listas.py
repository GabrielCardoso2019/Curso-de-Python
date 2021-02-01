valores = list()

while True:
    valores.append(int(input('Digite um valor: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip()[0].upper()
    if resp == 'N':
        break

if 5 in valores:
    temCinco = 'Tem o 5'
else:
    temCinco = 'Não tem o 5'

print('=-=' * 20)
valores.sort()
print(f'Você digitou: {len(valores)}. valores: {valores}')
valores.sort(reverse=True)
print(f'Os valores invertidos: {valores}')
print(f'{temCinco}')
