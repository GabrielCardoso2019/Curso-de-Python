num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))

if num1 > num2:
    print('\nO \033[1;31mprimeiro número\033[m {} é maior'.format(num1))
elif num2 > num1:
    print('O \033[1;31msegundo número\033[m {} é maior'.format(num2))
else:
    print('\033[1;31mNão existe\033[m valor maior, os dois são \033[1;34miguais\033[m')
