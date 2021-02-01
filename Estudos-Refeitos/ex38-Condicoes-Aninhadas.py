n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print(f'O número {n2} é maior que o segundo.')
elif n2 > n1:
    print(f'O número {n2} é maior que o primeiro.')
else:
    print(f'O primeiro e o segundo número, são iguais.')
