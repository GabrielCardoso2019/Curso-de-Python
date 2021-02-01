# =============================
# 1 - Interactive help
# 2 - Docstring
# 3 - Argumentos/Parâmetros opcionais
# 4 - escopo de variáveis
# 5 - retorno de resultados
# =============================

print('-=' * 30)
# =============================
# 1 - INTERACTIVE HELP
help(print)
print(input.__doc__) # Input doc


# =============================
print('-=' * 30)
# =============================
# 2 - DOCSTRING
def contador(i, f, p):
    """
    --> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return:  sem retorno
    Function created by Gabriel Cardoso
    """

    c = i
    while c <= f:
        print(f'{c}', end='.. ')
        c += p
    print('FIM!')

contador(2, 10, 2)
help(contador)


# =============================
print('-=' * 30)
# =============================
# 3 - ARGUMENTOS/PARÂMETROS OPCIONAIS
def somar(a=0, b=0, c=0):
    """
    --> Faz a soma de três valores e mostra o resultado na tela.
    :param a: O primeiro valor
    :param b: O segundo valor
    :param c: O terceiro valor
    Function created by Gabriel Cardoso
    """
    s = a + b + c
    print(f'A soma vale {s}')

# end='' é um parâmetro opcional

somar(3, 2, 5)
somar(8, 4)
somar()


# =============================
print('-=' * 30)
# =============================
# 4 - ESCOPO DE VARIÁVEIS
def teste():
    x = 8  # Variável local
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

n = 2  # variável global
print(f'No programa principal, n vale {n}')
teste()

print('=' * 10)
def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')

n1 = 2
funcao()
print(f'N1 fora vale {n1}')

print('=' * 10)
def teste2(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste2(a)
print(f'A fora vale {a}')


# =============================
print('-=' * 30)
# =============================
# 5 - RETORNO DE VARIÁVEIS
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

print(f'A soma dos valores é igual a {r1}, {r2}, {r3}')


# =============================
print('-=' * 30)
# =============================
# PRATICA

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são: {f1}, {f2}, {f3}.')
# n = int(input('Digite um número: '))
# print(f'O fatorial de {n} é igual a {fatorial(n)}')
print('=' * 10)

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
if par(num):
    print('É PAR')
else:
    print('É ÍMPAR')
