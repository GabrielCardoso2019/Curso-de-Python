lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# Tuplas são imutáveis
# lanche[1] = 'Refrigerante' <-- Não funciona
# print(lanche)

# trás do 1 ao 3 item
print(lanche[1:3])
# Trás do 1 ao 0 (Python ignora um número)
print(lanche[:2])
# Trás o 3º item de trás para frente
print(lanche[-3:])
# Mostra toda a tupla
print(lanche)
# Mostra quantos elementos existem na tupla
print(len(lanche))

print('=' * 20)

for cont in range(0, len(lanche)):
    print(lanche[cont])

print('-=' * 30)

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

print('-=' * 30)

for cont in range(0, len(lanche)):
    print(f'fEu vou comer {lanche[cont]} na posição  {cont}')

print('-=' * 30)

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi pra caramba!')

print('-=' * 30)

# Mostra a ordem em tamanho
print(sorted(lanche))
print(lanche)

print('=' * 20)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(len(c))
print(c.count(1))
print(c.index(2, 4))

print('=' * 20)

pessoa = ('Gabriel', 39, 'M', 1.71)
print(pessoa)

