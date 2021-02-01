num = int(input('Digite um número inteiro: '))

print('-=' * 20)
print(''' --- ESCOLHA UMA OPÇÃO ---
[ 1 ] CONVERTER PARA BÍNARIO
[ 2 ] CONVERTER PARA OCTAL
[ 3 ] CONVERTER PARA HEXADECIMAL''')

opc = int(input('Escolha uma opção acima: '))
print('-=' * 20)

if opc == 1:
    print(f'O número {num} para conversão em BÍNARIO é {bin(num)}')
elif opc == 2:
    print(f'O número {num} para conversão em OCTAL é {oct(num)}')
elif opc == 3:
    print(f'O número {num} para conversão em HEXADECIMAL é {hex(num)}')
else:
    print('\033[1;31mERR: Digite um número existente na lista\033[m.')
