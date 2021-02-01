# valores = list()
# dados = list()
# cont = 1

# for v in range(0, 7):
#    dados.append(int(input(f'Digite o {cont} valor: ')))
#    valores.append(dados[:])
#    dados.clear()
#    cont += 1

# for v in valores:
#    if v % 2 == 0:
#        par = dados.append(v)
#    elif v % 2 == 1:
#        impar = dados.append(v)

# print(f'Os valores pares são: {par.sort()}')
# print(f'Os valores ímpares são: {impar.sort()}')

# Lista interna
num = [[], []]
valor = 0

for c in range(1, 8):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 30)
print(f'Todos os valores: {num}')

