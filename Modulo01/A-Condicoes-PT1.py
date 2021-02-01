# Padrão Simplificado
tempo = int(input('Quantos anos tem seu carro? '))
print('carro novo' if tempo <= 3 else 'carro velho')

# Padrão Simples
""" if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--') """


nome = str(input('\nQual é seu nome? '))
if nome == 'Gabriel':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
    print('Bom dia, {}!'.format(nome))

# Padrão composto
n1 = float(input('\nDigite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
