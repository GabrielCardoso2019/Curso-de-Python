nome = str(input('Digite seu nome completo: '))
priNome = nome.split()
ultNome = len(priNome)
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é: {}'. format(priNome[0]))
print('Seu último nome é: {}'.format(priNome[ultNome-1]))