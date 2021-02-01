from datetime import datetime
pessoa = dict()

print('\033[1;31m---- CADASTRO DE TRABALHADOR ----\033[m')
pessoa['NOME'] = str(input('Digite o nome: '))
nasc = int(input('Digite o ano de nascimento: '))
pessoa['IDADE'] = datetime.now().year - nasc
pessoa['CTPS'] = int(input('Digite o número da sua CTPS (0 não tem): '))

if pessoa['CTPS'] != 0:
    pessoa['ANO DE CONTRATAÇÃO'] = int(input('Digite o ano de contração: '))
    pessoa['SÁLARIO'] = float(input('Digite o seu sálario: R$'))
    pessoa['APOSENTADORIA'] = pessoa['IDADE'] + ((pessoa["ANO DE CONTRATAÇÃO"] + 35) - datetime.now().year)
print('\033[1;31m-=\033[m' * 30)
for v, k in pessoa.items():
    print(f'    - \033[1m{v}\033[m tem o valor {k}')

