# int - 7, -4 ,0, 9875;
# float - 4.5, 0.076, -15.223, 7.0;
# bool - True, False;
# str - 'Olá', '7.5', '';

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))
s = n1 + n2

# print(type(n1))
# print('A soma entre', n1, 'e', n2, 'vale', s) <- Formato antigo do Python2

print('A soma entre {} e {} vale {}'.format(n1, n2, s))  # <- Formato mais recente

# Tipos Boolean
n = input('\nDigite um Valor: ')
print(n.isnumeric())  # <- Númerico

m = input('\nDigite outro: ')
print(m.isalpha())  # <- Alfabético

x = input('\nDigite outro valor: ')
print(x.isalnum())  # <- Alfabético e Númerico
