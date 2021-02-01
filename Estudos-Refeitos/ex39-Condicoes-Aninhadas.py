from datetime import date
from time import sleep

print('-=' * 20)
print('           ALISTAMENTO MILITAR')
print('-=' * 20)

nome = str(input('Digite seu nome: '))
anoNasc = int(input('Digite seu ano de nascimento: '))
idadeAtual = date.today().year - anoNasc

print('-=' * 20)
print('           PROCESSANDO...')
sleep(2)
print('-=' * 20)

if idadeAtual > 18:
    saldo = idadeAtual - 18
    print(f'Olá {nome}. Atualmente você tem {idadeAtual} anos e já se passou {saldo} anos para o alistamento.')
elif idadeAtual < 18:
    saldo = 18 - idadeAtual
    print(f'Olá {nome}. Atualmente você tem {idadeAtual} anos e faltam {saldo} anos para o seu alistamento')
elif idadeAtual == 18:
    print(f'Olá {nome}. Atualmente você tem {idadeAtual} anos e chegou o momento de se alistar')
else:
    print(f'Olá {nome}. Você já tem 18 anos, está na hora de ir a junta militar para o alistamento.')
