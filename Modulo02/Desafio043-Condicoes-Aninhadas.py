print('-=-' * 20)
print('Calculo de IMC')
print('-=-' * 20)

nome = str(input('Digite seu nome: '))
peso = float(input('Digite seu peso: Kg '))
altura = float(input('Digite a sua altura: '))

imc = (peso / (altura * altura))
cores = {'limpa': '\033[m',
         'vermelho': '\033[1;31m',
         'Verde': '\033[1;32m',
         'Amarelo': '\033[1;33m'}

if imc <= 18.5:
    print('Seu IMC é de {:.2f}. {}{} você está abaixo do peso{}'.format(imc, cores['vermelho'], nome, cores['limpa']))
elif imc <= 25.0:
    print('Seu IMC é de {:.2f}. {}{} você está no peso ideal{}'.format(imc, cores['Verde'], nome, cores['limpa']))
elif imc <= 30.0:
    print('Seu IMC é de {:.2f}. {}{} você está com sobrepeso{}'.format(imc, cores['Amarelo'], nome, cores['limpa']))
elif imc <= 40.0:
    print('Seu IMC é de {:.2f}. {}{} você está com obesidade{}'.format(imc, cores['Amarelo'], nome, cores['limpa']))
else:
    print('Seu IMC é de {:.2f}. '
          '{}{} você está com obesidade mórbida{}'.format(imc, cores['vermelho'], nome, cores['limpa']))



