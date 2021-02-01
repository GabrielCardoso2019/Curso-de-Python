from time import sleep

print('-=-' * 10)
print('{:^30}'.format('G`CARDOSO STORE CAR'))
print('-=-' * 10)

produto = str(input('Digite qual é o produto: '))
preco = float(input('Digite o valor do produto: R$'))

print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opcao = int(input('Qual é a opção desejada? '))

print()
print('PROCESSANDO DADOS...')
sleep(2)
print()

if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('O produto {} será parcelado em 2x de R${:.2f} SEM JUROS'.format(produto, parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalparc = int(input('Quantas Parcelas? '))
    parcela = total / totalparc
    print('Sua compra do produto {} será parcelada em {}x de R${:.2f} COM JUROS'.format(produto, totalparc, parcela))
else:
    total = 0
    print('OPÇÃO INVÁLIDA DE PAGAMENTO. TENTE NOVAMENTE!')

print('Sua compra do produto {} custava R${:.2f} e vai custar R${:.2f} no final'.format(produto, preco, total))
