velocidade = float(input('Qual é a velocidade atual do carro? '))

if velocidade > 80:
    print('\033[1;31mMULTADO! Você exedeu o limite permitido que é de 80Km/h\033[m')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de \033[1;31;40mR${:.2f}\033[m'.format(multa))
else:
    print('\033[1;32mTenha um ótimo dia! Dirija sempre com segurança\033[1;32m')
