num = int(input('Digite um número inteiro: '))

print('-=-' * 20)
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')

opcao = int(input('\nEscolha uma opção: '))
print('-=-' * 20)

if opcao == 1:
    print('{} converção para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} converção para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} converção para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente!')

