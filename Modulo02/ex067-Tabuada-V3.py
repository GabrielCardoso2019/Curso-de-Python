print('-=-' * 20)
print('ESCOLHA SUA TABUADA')
print('-=-' * 20)

while True:
    num = int(input('Digite o número da tabuada. \033[1;31mValores negativos param o programa\033[m:  '))
    if num < 0:
        break
    print('-' * 30)
    for cont in range(1, 11):
        print(f'{num} X {cont} = {num*cont}')
    print('-' * 30)
print('PROGRAMA DE TABUADA ENCERRADO. VOLTE SEMPRE!')
