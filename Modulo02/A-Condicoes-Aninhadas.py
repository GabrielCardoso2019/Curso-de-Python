"""if condicao:
    elif:
        condicao
    elif:
        condicao
else:
condicao final"""

nome = str(input('Qual é o seu nome? '))
if nome == 'Gabriel':
    print('Que belo nome!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Tenha um bom dia, {}!'.format(nome))
