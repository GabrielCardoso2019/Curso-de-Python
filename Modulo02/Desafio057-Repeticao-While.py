s = ''
while s != 'Mm' or s != 'Ff':
    s = str(input('Digite seu sexo [M/F]: ')).upper()
    if s in 'Mm':
        print('\033[1;33mVocê é Homem\033[m')
    elif s in 'Ff':
        print('\033[1;31mVocê é Mulher\033[m')
    else:
        print('DIGITE UM VALOR VÁLIDO!!!')
print('FIM')
