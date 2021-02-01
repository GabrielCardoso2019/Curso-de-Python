"""def arqExist(name):
    try:
        # r - read; t - text
        a_file = open(name, 'rt')
        a_file.close()
    except FileNotFoundError:
        return False
    else:
        return True

def createArq(name):
    try:
        # w = write; t = text; + = criar
        a_file = open(name, 'wt+')
    except:
        print('\033[1;31mERR: HOUVE UM ERRO NA CRIAÇÃO DO ARQUIVO\033[m')
    else:
        print(f'ARQUIVO {name} CRIADO COM SUCESSO')


a_file = 'nomes.txt'
if not arqExist(a_file):
    createArq(a_file)


def register(msg):
    cont = 0
    while True:
        nome = str(input(msg))
        if nome == '999':
            print('PROGRAMA FINALIZADO')
            break
        try:
            a_file = open("nomes.txt", "at")
        except:
            print('HOUVE UM PROBLEMA AO ABRIR O ARQUIVO')
        else:
            try:
                a_file.write(f'{cont + 1}, {nome}\n')
                cont += 1
            except:
                print('HOUVE UM PROBLEMA AO ESCREVER NO ARQUIVO')
        finally:
            a_file.close()

def readfile():
    try:
        a_file = open("nomes.txt", "rt")
    except:
        print('HOUVE UM PROBLEMA AO ABRIR O ARQUIVO')
    else:
        try:
            for lines in a_file:
                print(f'{lines}')
        finally:
            a_file.close()

def delete(msg):
    try:
        a_file = open("nomes.txt", "at")
        line = a_file.readLines()
    except:
        print('HOUVE ALGUM PROBLEMA')
    else:
        num = int(input(msg))
        del line[num]


register('Digite seu nome: ')
readfile()
delete('Digite o número do nome para deletar: ')"""

a_file = open("sample.txt", "r")
lines = a_file.readlines()
a_file.close()


def delete(msg):
    numero = int(input(msg))
    try:
        a_file = open("sample.txt", "rt")
    except:
        print('houve um erro')
    else:
        try:
            del lines[numero]
        except:
            print('houve um erro ao deletar')
        else:
            new_file = open("sample.txt", "w+")
            for line in lines:
                new_file.write(line)
    finally:
        new_file.close()


delete('digite um número: ')
