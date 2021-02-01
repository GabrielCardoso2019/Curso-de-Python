n1 = float(input('Comprimento da 1º reta: '))
n2 = float(input('Comprimento da 2º reta: '))
n3 = float(input('Comprimento da 3º reta: '))

if n1 == n2 and n2 == n3:
    print('As retas {}, {} e {} formam um triâgulo Equilátero.'.format(n1, n2, n3))
elif n1 == n2 and n3 != n1 + n2 or n2 == n3 and n1 != n2 + n3:
    print('As retas {}, {} e {} formam um triâgulo Isósceles.'.format(n1, n2, n3))
elif n1 < n2 + n3 and n2 < n3 + n1 and n3 < n1 + n2:
    print('As retas {}, {} e {} formam um triâgulo Escaleno.'.format(n1, n2, n3))
else:
    print('As retas informadas não formam um trinângulo!')
