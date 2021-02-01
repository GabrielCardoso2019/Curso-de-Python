# + <- adição
# - <- Subtração
# * <- Multiplicação
# / <- Divisão
# ** <- Potência
# // Divisão Inteira
# % <- Resto da Divisão

# Ordem de precedência
# 1 <- ()
# 2 <- **
# 3 <- *  /  //   %
# 4 <- +  -

nome = input('Qual o seu nome? ')
print('Prazer em te conhecer {:=^20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:<20}!\n'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}'.format(di, e))

# \n <- Quebra de linha
# end= ' ' <- Coloca tudo na mesma linha
