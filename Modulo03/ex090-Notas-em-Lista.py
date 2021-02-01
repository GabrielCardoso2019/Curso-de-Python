aluno = dict()
aluno['Nome'] = str(input('Digite o nome do(a) aluno(a): '))
aluno['Média'] = float(input(f'Média do(a) {aluno["Nome"]}: '))

if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'

print('-=' * 30)
for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')
