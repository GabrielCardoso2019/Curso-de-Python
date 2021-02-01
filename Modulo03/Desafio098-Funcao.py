from time import sleep
cont = 10
print('-=' * 20)
print('Contagem de 1 até 10 de 1 em 1')
for n in range(1, cont+1):
    sleep(0.5)
    print(f'{n}', end=' ')
print('FIM!')

print('-=' * 20)
print('Contagem de 10 até 0 de 2 em 2')
for n in range(cont, -1, -2):
    sleep(0.5)
    print(f'{n}', end=' ')
print('FIM!')

def contador(inicio, fim, passo):
    print(f'Contagem de {i} até {f} de {p} em {p}')
    for num in range(inicio, fim+1, passo):
        sleep(0.5)
        print(f'{num} ', end='')
    print('FIM!')
print('-=' * 20)

print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
print('-=' * 20)
contador(i, f, p)
