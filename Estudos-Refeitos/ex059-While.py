from time import sleep

valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))

opcao = 0
while opcao != 5:
    print(''' ------------ESCOLHA UMA DAS OPÇÕES ABAIXO:------------
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA 
    ''')
    opcao = int(input('Digite uma opção: '))

    if opcao == 1:
        soma = valor1 + valor2
        print(f'A soma dos valores {valor1} e {valor2} é igual a {soma}')
    elif opcao == 2:
        mult = valor1 * valor2
        print(f'A multiplicação dos valores {valor1} e {valor2} é igual a {mult}')
    elif opcao == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print(f'O maior valor entre {valor1} e {valor2} é {maior}')
    elif opcao == 4:
        print('INFORME NOVOS VALORES')
        valor1 = int(input('Digite um novo valor: '))
        valor2 = int(input('Digite outro novo valor: '))
    elif opcao == 5:
        print('FINALIZANDO...')
        sleep(2)
    else:
        print('Opção inválida. Digite um valor válido')
print('OPERAÇÃO FINALIZADA')
