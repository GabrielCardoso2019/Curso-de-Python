from time import sleep

print('-=' * 20)
print('EMPRESTIMO BANCOS SANTANDER')
print('-=' * 20)

nomeComprador = str(input('Digite seu nome: '))
valorCasa = float(input('Digite o valor da Casa: R$'))
salario = float(input('Digite o seu sálario: R$'))
PgtoAno = int(input('Digite em quantos anos irá pagar: '))

prestacao = valorCasa / (PgtoAno * 12)
minimo = salario * 30 / 100

print('-=' * 20)
print('PROCESSANDO...')
sleep(2)
print('-=' * 20)

print(f'Sr.(Sra) {nomeComprador}, para pagar uma casa de R${valorCasa:.2f} em {PgtoAno} anos.', end='')
print(f'A prestação será de R${prestacao:.2f} reais.')
print(f'COMPRANDO tem que pagar {prestacao:.2f} e o mínimo é de {minimo:.2f}')

if prestacao <= minimo:
    sleep(2)
    print('\033[1;32mEMPRESTIMO CONCEDIDO COM SUCESSO!\033[m')
else:
    sleep(2)
    print('\033[1;31mEMPRESTIMO NEGADO\033[m')
