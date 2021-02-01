valores = list()

for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para posição {cont}: ')))
print(f"Seus valores foram {valores}")
print(f'O maior valor digitado foi {max(valores)} e o menor foi {min(valores)}')

print('\n==== Posição dos números: ====')
for co, va in enumerate(valores):
    print(f'na posição {co} encontrei o {va}...')
print(f'{"Cheguei o final da lista".upper()}')
