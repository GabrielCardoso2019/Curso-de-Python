def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[1;31mERR! O valor digitado é inválido. '
                  'Digite um número inteiro\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'O número que você digitou foi {n}')
