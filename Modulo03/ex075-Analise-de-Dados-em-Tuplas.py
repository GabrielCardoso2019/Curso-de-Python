num = (int(input('Digite um número: ')),
       int(input('Digite um outro número: ')),
       int(input('Digite mais o número: ')),
       int(input('Digite só mais um número: ')))

print(f'O valor 9 aparece {num.count(9)}')
if 3 in num:
    print(f'O número 3 aparece {num.index(3)} vezes')
else:
    print(f'O número 3 não foi digitado')
print(f'Os números pares são, ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
    else:
        n = 0
        print(f'Existem {n} números pares')
