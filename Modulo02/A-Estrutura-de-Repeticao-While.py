"""for c in range(1, 10):
    print(c)
print('THE END')"""

'''WHILE se usa quando não se sabe o limite'''
# c = 1
# num = int(input('Digite um numero: '))
# while c < num+1:
#     print(c)
#     c += 1
# print('THE END')

'''Condição com valor diferente'''
# n = 1
# while n != 0:
#    n = int(input('Digite um valor: '))
# print('FIM')

'''Condição com texto'''
# r = 'S'
# while r == 'S':
#    n = int(input('Digite um numero: '))
#    r = str(input('Quer continuar? [S/N] ')).upper()
# print('FIM')


n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))
