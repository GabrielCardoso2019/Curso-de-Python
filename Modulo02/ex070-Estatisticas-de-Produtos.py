total = totmil = totmenor = cont = 0
barato = ''

while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < totmenor:
        totmenor = preco
        barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print('{:-^40}'.format(' FIM DA COMPRA '))
print(f'O total da compra foi R${total:.2f}')
print(f'O produto mais barato foi {barato} que custa R${totmenor:.2f} reais')
print(f'Temos {totmil} custando mais de R$1.000,00 reais')
