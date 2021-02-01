def area(larg, comp):
    a = l * c
    print(f'A área dos valores {larg} X {comp} é equivalente ao terreno de {a}m²')

print('---- CALCULO DE TERRENO ----')
print('-=-' * 20)

l = float(input('LARGURA (M): '))
c = float(input('COMPRIMENTO (M): '))
area(l, c)
