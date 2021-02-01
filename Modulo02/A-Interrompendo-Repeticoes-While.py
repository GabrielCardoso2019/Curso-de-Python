"""cont = 1
while cont <= 10:
    print(cont, '-> ', end='')
    cont += 1
print('ACABOU')"""

"""n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
# print('A soma vale {}'.format(s))
print(f'A soma vale {s}')"""

nome = 'José'
idade = 33
salario = 2560.50
print(f'O {nome} tem {idade} anos e ganha {salario:.2f}')  # PYTHON 3.6+
print('O {} tem {} anos e ganha {:.2f}'.format(nome, idade, salario))  # PYTHON 3
