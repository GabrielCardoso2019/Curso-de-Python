# ===============================================
#
#           ESTUDOS NO LIVRO DE PYTHON
#
# ===============================================

def soma(a, b):
    print(a + b)

soma(2, 9)
soma(7, 8)
soma(10, 15)

# ===============================================
print('-=' * 20)
# ===============================================
# RETORNO DE VALOR DA FUNÇÃO
def soma(a, b):
    return a + b
print(soma(2, 9))

# ===============================================
print('-=' * 20)
# ===============================================
# RETORNO DE VALOR DA FUNÇÃO - TRUE OR FALSE
"""def epar(x):
    return x % 2 == 0
print(epar(2))
print(epar(3))
print(epar(10))"""

def epar(x):
    return x % 2 == 0
def par_ou_impar(x):
    if epar(x):
        return "PAR"
    else:
        return "ÍMPAR"
print(par_ou_impar(4))
print(par_ou_impar(5))

# ===============================================
print('-=' * 20)
# ===============================================
# RETORNO DE VALOR DA FUNÇÃO - EX 8.1
def maiorNumero(a, b):
    c = 0
    if a > b:
        c = a
    else:
        c = b
    return c
print(maiorNumero(5, 4))
print(maiorNumero(3, 1))

# ===============================================
print('-=' * 20)
# ===============================================
# RETORNO DE VALOR DA FUNÇÃO - EX 8.2 - MÚLTIPLOS
def emult(a, b):
    return a % b == 0
print(emult(8, 4))
print(emult(7, 3))
print(emult(7, 7))

# ==================================================
print('-=' * 20)
# ==================================================
# RETORNO DE VALOR DA FUNÇÃO - EX 8.3 - AO QUADRADO²
def quad(x):
    return x ** 2
print(quad(4))
print(quad(9))

# ===============================================
print('-=' * 20)
# ===============================================
# RETORNO DE VALOR DA FUNÇÃO - EX 8.4 - TRIÂNGULO
def base(a, b):
    return (a * b) / 2
print(base(6, 9))
print(base(5, 8))

# ===============================================
print('-=' * 20)
# ===============================================
# RETORNO DE VALOR DA FUNÇÃO - PESQUISA EM LISTA
def pesquise(lista, valor):
    for x, e in enumerate(lista):
        if e == valor:
            return x
    return None
L = [10, 20, 25, 30]
print(pesquise(L, 25))
print(pesquise(L, 27))

# ========================================================================
print('-=' * 20)
# ========================================================================
# RETORNO DE VALOR DA FUNÇÃO - CALCULANDO A MÉDIA DOS VALORES DE UMA LISTA
def soma(l):
    total = 0
    for e in l:
        total += e
    return total
def media(l):
    return soma(l) / len(l)

# ========================================================================
print('-=' * 20)
# ========================================================================
# RETORNO DE VALOR DA FUNÇÃO - CALCULO FATORIAL
def fatorial(n):
    fat = 1
    while n > 1:
        fat *= n
        n -= 1
    return fat
print(fatorial(5))

# OUTRA FORMA DE CALCULO FATORIAL
def fatorial(n):
    fat = x = 1
    while x <= n:
        fat *= x
        x += 1
    return fat
print(fatorial(10))

# ========================================================================
print('-=' * 20)
# ========================================================================
# RETORNO DE VALOR DA FUNÇÃO - EX 8.5



