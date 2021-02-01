result = 0
cont = 0
for i in range(1, 7):
    num = int(input('Digite um valor: '))
    result += num
    cont += 1
print('O somatório de {} todos os valores foi de {}'.format(cont, result))
