valores = list()

while True:
    n = int(input('Digite um valor: '))
    # Se o n não estiver nos valores
    if n not in valores:
        valores.append(n)
        print('Adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')

    r = str(input('Quer continuar? [S/N] '))
    # Se minha resposta estiver em 'Nn'
    if r in 'Nn':
        break

print('-=' * 30)
valores.sort()
print(f'Seus valores são {valores}')
