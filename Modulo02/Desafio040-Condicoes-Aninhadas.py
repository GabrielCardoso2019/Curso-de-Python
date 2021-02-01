from time import sleep

print('-=-' * 20)
print('Calculando Média')
print('-=-' * 20)

nomeAluno = str(input('Nome do aluno: '.upper()))
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

mediaTotal = (nota1 + nota2) / 2

cores = {'limpa': '\033[m',
         'Vermelho': '\033[1;31m',
         'Verde': '\033[1;32m',
         'Amarelo': '\033[1;33m'}

print()
print('PROCESSANDO...')
sleep(3)
print()

if mediaTotal < 5:
    print('{}O ALUNO(a) {} FOI REPROVADO(a){}'.format(cores['Vermelho'], nomeAluno, cores['limpa']))
elif mediaTotal >= 7:
    print('{} O ALUNO(a) {} É FORA DA CURVA. APROVADO(a)!{}'.format(cores['Verde'], nomeAluno, cores['limpa']))
else:
    print('{}O ALUNO(a) {} FICOU DE RECUPERAÇÃO{}'.format(cores['Amarelo'], nomeAluno, cores['limpa']))

