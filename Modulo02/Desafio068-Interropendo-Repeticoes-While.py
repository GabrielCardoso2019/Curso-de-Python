from random import randint

print('=-=' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-=' * 20)

v = 0
while True:
    computador = randint(1, 10)
    jogador = int(input('Digite um valor: '))
    total = computador + computador

    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('PAR ou ÍMPAR? [P/I] ')).upper().strip()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')
