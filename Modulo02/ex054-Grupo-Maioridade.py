from datetime import date

atual = date.today().year
totalMaior = 0
totalMenor = 0

for pessoa in range(1, 8):
    nasc = int(input('Em que ano a pessoa {}ª nasceu? '.format(pessoa)))
    idade = atual - nasc
    if idade >= 21:
        totalMaior += 1
    else:
        totalMenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totalMaior))
print('E também tivemos {} pessoas menores de idade'.format(totalMenor))
