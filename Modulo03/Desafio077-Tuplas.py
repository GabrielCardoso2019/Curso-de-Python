palavras = ('Python', 'Aprender', 'Programar', 'Java', 'Praticar', 'UML',
            'Diagrama', 'Amiga', 'Maseratti', 'Futuro', 'Trabalhar')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
print('\nAcabou!')
