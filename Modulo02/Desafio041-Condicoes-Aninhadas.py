from datetime import date
from time import sleep

print('-=-' * 20)
print('CONFEDERAÇÃO DE NATAÇÃO PROFISSIONAL')
print('-=-' * 20)

anoNascimento = int(input('Digite o ANO de nascimento: '))
idade = (date.today().year - anoNascimento)

print()
print('PROCESSANDO...')
sleep(2)
print()

if idade <= 9:
    print('Nadador Mirim')
elif idade <= 14:
    print('Nadador Infantil')
elif idade <= 19:
    print('Nadador Junior')
elif idade <= 20:
    print('Nadador Sênior')
else:
    print('Nadador Master')
