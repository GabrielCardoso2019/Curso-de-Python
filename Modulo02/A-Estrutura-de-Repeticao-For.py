# Repetição do i 5 vezes
for i in range(0, 5):
    print('Oi')
print('FIM')

# Contagem Padrão
for i in range(1, 7):
    print(i)
print('FIM')

# Contagem Contraria
for i in range(7, 0, -1):
    print(i)
print('FIM')

# Usando variável
# Contagem em saltos
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
# n = int(input('Digite um número: '))
for i in range(inicio, fim+1, passo):
    print(i)
print('FIM')

# Faz o programa ler até o range 3. Apenas a quantidade do range
for i in range(0, 3):
    n = int(input('Digite um valor: '))
print('FIM')

# Faz o programa ler o range até o 4 e faz o somatório
r = 0
for i in range(0, 4):
    n = int(input('Digite um valor: '))
    r += n
print('O somatório de todos os valores foi {}'.format(r))

