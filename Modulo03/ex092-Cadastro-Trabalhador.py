from datetime import datetime

dados = dict()
dados['NOME'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['IDADE'] = datetime.now().year - nasc
dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['CTPS'] != 0:
    dados['CONTRATAÇÃO'] = int(input('Ano de Contratação: '))
    dados['SALÁRIO'] = float(input('Salário: R$'))
    dados['APOSENTADORIA'] = dados['IDADE'] + ((dados['CONTRATAÇÃO'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f'    - {k} tem o valor {v}')
