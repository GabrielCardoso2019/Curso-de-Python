from datetime import date
from time import sleep

print('-=-' * 20)
print('Alistamento Militar')
print('-=-' * 20)

nome = str(input('Digite seu nome: '))
anoNascimento = int(input('Digite seu ano de nascimento: '))

idadeAtual = (date.today().year - anoNascimento)

print()
print('PROCESSANDO ANO...')
sleep(3)
print()

if idadeAtual < 18:
    saldo = 18 - idadeAtual
    print('Olá, {}. Você tem {} anos e faltam {} anos para o  alistamento.'.format(nome, saldo, idadeAtual))
elif idadeAtual > 18:
    saldo = idadeAtual - 18
    print('{} você tem {} anos e já passou {} anos para se alistar'.format(nome, saldo, idadeAtual))
elif idadeAtual == 18:
    print('Olá {} chegou o momento do seu alistamento militar'.format(nome))
else:
    print('{} você já tem 18 anos, está na hora de se alistar jovem'.format(nome))
