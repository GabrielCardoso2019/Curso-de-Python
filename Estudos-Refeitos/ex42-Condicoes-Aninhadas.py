def espaco(msg):
    tam = len(msg)
    print('-' * tam)
    print('Analisador de Triângulos')
    print('-' * tam)


r1 = int(input('Primeiro segmento: '))
r2 = int(input('Segundo segmento: '))
r3 = int(input('Terceiro segmento: '))

if r1 == r2 and r2 == r3:
    print(f'As retas {r1}, {r2}, {r3} formam um triâgulo Equilátero.')
elif r1 == r2 and r3 != r1 + r2 or r2 == r3 and r1 != r2 + r3:
    print(f'As retas {r1}, {r2} e {r3} formam um triâgulo Isósceles.')
elif r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print(f'As retas {r1}, {r2} e {r3} formam um triâgulo Escaleno.')
else:
    print('As retas informadas não formam um trinângulo!')
