from interface import *
from arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arqExiste(arq):
    criarArq(arq)

# Programa Principal
while True:
    resposta = menu(['Listar Pessoas', 'Cadastrar Pessoas', 'Sair'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        lerAqr(arq)
    elif resposta == 2:
        # Opção para cadastrar nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        cabecalho('\033[1;31mERR: Digite uma opção válida!\033[m')
    sleep(2)
