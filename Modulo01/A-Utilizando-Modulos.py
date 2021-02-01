# import math Importa tudo
from math import sqrt, floor

num = int(input('Digite um número: '))
raiz = sqrt(num)

# Arredonda para cima (math.ceil())
print('A raiz de {} é igual a {}'.format(num, raiz))

# Arredonda para baixo (math.floor())
print('\nA raiz de {} é igual a {}'.format(num, floor(raiz)))

# Padrão
print('\nA raiz de {} é igual a {:.2f}'.format(num, raiz))
