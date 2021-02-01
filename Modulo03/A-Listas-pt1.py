# tuplas usa ()
# listas usa []

num = (2, 5, 9, 1)
# num[2] = 3 <- Tupla são imutáveis
print(num)

num2 = [2, 5, 9, 1]
num2.append(7)  # <- Adiciona o número 7
num2.sort()  # <- Organiza os números em ordem
print(num2)

num3 = [2, 5, 9, 1]
num3.sort(reverse=True)  # <- Faz os números ficarem ao contrário
print(num3)

print(f'Essa lista tem {len(num3)} elementos')  # <- Quantidade de elementos na lista

# 2 = Posição & 0 = Número add
num3.insert(2, 2)  # <- Insere um valor em uma posição existente
print(num3)

# Elimina a primeira ocorrêcia (sem laços)
num3.remove(2)
print(num3)

if 5 in num3:
    num3.remove(5)
else:
    print('Não achei o número 5')

# remoção de valor
num3.pop(2)
print(num3)

# ====================================================
print('===' * 15)
# ====================================================

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'na posição {c} encontrei o {v}...')
print('Cheguei o final da lista')

# ====================================================
print('===' * 20)
# ====================================================

valor = list()
for cont in range(0, 5):
    valor.append(int(input('Digite um valor: ')))

for co, va in enumerate(valor):
    print(f'na posição {co} encontrei o {va}...')
print('Cheguei o final da lista')

# ====================================================
print('===' * 15)
# ====================================================

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
