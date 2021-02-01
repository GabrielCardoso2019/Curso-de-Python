salario = float(input('Digite seu sálario: '))

if salario > 1250:
    print('Seu sálario ganhou um aumento de 10% e agora você ganha {}'.format(salario * 1.10))
else:
    print('Seu salário ganhou um aumento de 15% e agora você ganha {}'.format(salario * 1.15))
