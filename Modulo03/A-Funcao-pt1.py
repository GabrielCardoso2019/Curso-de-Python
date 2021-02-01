def lin():
    print('-' * 20)

# Programa Principal
lin()
print(' Gabriel Cardoso ')
lin()
print(' Dev Python ')
lin()
print(' I LOVE TIVIT ')
lin()

# =========================================
print('=-=' * 30)
# Função com parâmetros
def mensagem(msg):
    print('-' * 20)
    print(msg)
    print('-' * 20)

mensagem('SISTEMA DE ALUNOS')
print()

def titulo(txt):
    print('-' * 20)
    print(txt)

titulo(' Curso em Video ')
titulo(' Python é Vida')
titulo(' PYTHON É MELHOR QUE JAVA')

# =========================================
print('=-=' * 30)
# soma de valores pelos parametros
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')

soma(b=4, a=5)
soma(7, 2)
soma(3, 9)

# =========================================
print('=-=' * 30)
# Empacotamento de parâmetros
# * num é o desempacotamento
def contador(* num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')
    print('-' * 10)

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

# =========================================
print('=-=' * 30)
# usando lista
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6, 8, 2, 4, 3, 1]
dobra(valores)
print(valores)
