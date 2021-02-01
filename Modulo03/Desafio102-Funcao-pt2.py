def fatorial(num=1, show=False):
    """
    --> Calcula o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (Opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')

        f *= c
    return f

# Programa Principal
print(fatorial(10))
print(fatorial(10, show=True))
print()
print(' ======= HELP FUNCTION ======= ')
help(fatorial)
