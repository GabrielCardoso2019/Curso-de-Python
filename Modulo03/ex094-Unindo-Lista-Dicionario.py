galera = list()
pessoa = dict()
soma = media = 0

while True:
    pessoa['NOME'] = str(input('Nome: '))
    while True:
        pessoa['SEXO'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['SEXO'] in 'MF':
            break
        print('\033[1;31mERR! Por favor, digite apenas M ou F.\033[m')
    pessoa['IDADE'] = int(input('Idade: '))
    soma += pessoa['IDADE']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('\033[1;31mERR! Responda apenas com S ou N.\033[m')
    if resp == 'N':
        break

print('-=' * 30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'A média de idade é de {media:5.2f} anos.')
print('As mulheres cadastradas foram ', end='')
for p in galera:
    if p['SEXO'] in 'Ff':
        print(f'{p["NOME"]}, ', end='')
print()
print('Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['IDADE'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('\033[1m<<ENCERRADO>>\033[m')


