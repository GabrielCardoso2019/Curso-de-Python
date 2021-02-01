city = str(input('Digite o nome de uma cidade: '))
citySantos = city.upper().slipt()
citySantos = 'SANTO' in citySantos[0]
print('Inicia com Santos? {}'.format(citySantos))
