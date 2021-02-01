salario = float(input('Digite o seu sálario para o ajuste. R$'))

if salario > 1250.0:
    salario = salario + (salario * 10 / 100)
    print(f'Seu salario teve um aumento de 10%. Você passa a receber {salario}')
if salario < 1250.0:
    salario = salario + (salario * 15 / 100)
    print(f'Seu salario teve um aumento de 15%. Você passa a receber {salario}')
