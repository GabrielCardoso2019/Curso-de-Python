from time import sleep

c = ('\033[m',         # 0 - sem cores
     '\033[0;30;41m',  # 1 - cor vermelho
     '\033[0;30;42m',  # 2 - cor verde
     '\033[0;30;43m',  # 3 - cor amarelo
     '\033[0;30;44m',  # 4 - cor azul
     '\033[0;30;45m',  # 5 - cor roxa
     '\033[7;30m',     # 6 - cor branca
     )

def ajuda(com):
    titulo(f'ACESSANDO O MANUAL DO COMANDO \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)

# Programa Principal
comando = ''
while True:
    titulo('--- SISTEMA DE AJUDA PyHELP ---')
    comando = str(input('Função ou Biblioteca >>> '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO')
