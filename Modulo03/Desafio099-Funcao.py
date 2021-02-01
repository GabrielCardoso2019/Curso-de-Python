from time import sleep

print('-=' * 20)
def maior(* num):
    cont = maiorNum = 0
    print('Analisando os valores passados...')
    for n in num:
        tam = len(num)
        sleep(0.5)
        print(f'{n}', end=' ')
        if cont == 0:
            maiorNum = n
        else:
            if n > maiorNum:
                maiorNum = n
        cont += 1
    print(f'Foram informados {tam} valores ao todo.')
    print(f'O maior valor informado foi {maiorNum}.')
    print('-=' * 20)

maior(2, 7, 10, 5, 0, 3)
maior(7, 3, 5, 4, 2)
maior(5, 2, 1, 4)
maior(4, 1, 2)
maior(2, 1)
maior(0)
