"""
Exemplo -> \033[0;30;41m
0  - Style Text
30 - Color Text
41 - Background

======== STYLE TEXT ==========
0 - None
1 - Bold
4 - Underline
7 - Negative

======== COLOR TEXT ==========
30 - Branco
31 - Vermelho
32 - Verde
33 - Amarelo
34 - Azul claro
35 - Lilas
36 - Azul Ciano
37 - Cinza

======== BACKGROUND =========
40 - Branco
41 - Vermelho
42 - Verde
43 - Amarelo
44 - Azul claro
45 - Lilas
46 - Azul Ciano
47 - Cinza
"""

print('\033[7;33;44mOlá, Mundo!\033[m')

a = 3
b = 5
print('\nOs valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))

nome = 'Gabriel'
print('\nMuito prazer em te conhecer, {}{}{}'.format('\033[1;34m', nome, '\033[1;34m'))

nome2 = 'Gabriel'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoBranco': '\033[7;30m'}
print('\nMuito prazer em te conhecer, {}{}{}'.format(cores['pretoBranco'], nome, cores['limpa']))
