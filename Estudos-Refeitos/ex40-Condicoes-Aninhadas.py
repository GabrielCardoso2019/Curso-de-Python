from time import sleep

print('-=' * 20)
print('MÉDIA ESCOLAR')
print('-=' * 20)

nomeAluno = str(input('Digite o nome do aluno: '))
primeiraNota = float(input('Digite a primeira nota: '))
segundaNota = float(input('Digite a segunda nota: '))

media = (primeiraNota + segundaNota) / 2

print('-=' * 20)
print('BUSCANDO NO BANCO...')
sleep(2)
print('PROCESSANDO DADOS...')
sleep(2)
print('-=' * 20)

if media > 7.0:
    print(f'O(A) ALUNO(A) {nomeAluno} FOI APROVADO.')
elif media > 5.0 or media < 7.0:
    print(f'O(A) ALUNO(A) {nomeAluno} FICOU DE RECUPERAÇÃO')
else:
    print(f'O(A) ALUNO(A) {nomeAluno} FOI REPROVADO')





