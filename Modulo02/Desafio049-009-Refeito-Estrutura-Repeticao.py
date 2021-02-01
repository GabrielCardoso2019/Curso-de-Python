valor = int(input('Digite um valor: '))
r = 0
for i in range(0, 11):
    r = valor * i
    print('{} X {} = {}'.format(i, valor, r))
print('\nFIM')
