from time import sleep
from datetime import date

# Função de espaçamento
def espaco(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)


# Programa Principal
espaco('CNN - CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
sleep(2)

anoNasc = int(input('Digite o ano de nascimento: '))
idadeNivel = (date.today().year - anoNasc)

espaco('PROCESSANDO NÍVEL...')
sleep(2)

if idadeNivel <= 9:
    print('Seu nível na CONFEDERÇÃO é de MIRIM')
elif idadeNivel <= 14:
    print('Seu nível na CONFEDERAÇÃO é de INFANTIL')
elif idadeNivel <= 19:
    print('Seu nível na CONFEDERAÇÃO é de JUNIOR')
elif idadeNivel <= 20:
    print('Seu nível na CONFEDERAÇÃO é de SÊNIOR')
else:
    print('Seu nível na CONFEDERAÇÃO é de MASTER')
