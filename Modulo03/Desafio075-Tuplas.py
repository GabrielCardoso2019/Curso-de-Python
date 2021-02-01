num = (int(input('Digite um número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite outro número: ')))
print(f'Você digitou os valor: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'A posição do valor 3 é {num.index(3)+1}ª')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
