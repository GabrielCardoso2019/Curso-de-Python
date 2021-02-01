aluno = dict()
aluno['Nome'] = str(input('Digite o nome do(a) aluno(a): '))
aluno['Média'] = float(input(f'Digite a média do(a) {aluno["Nome"]}: '))

if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif aluno['Média'] >= 6:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado(a)'

print('-=' * 30)
for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')
