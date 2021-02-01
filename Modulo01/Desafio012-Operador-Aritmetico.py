nomeProd = input('Digite qual é o produto: ')
valorProd = float(input('Digite o valor do produto: '))

descontoProd = valorProd * 0.95
print('O seu produto: {} custa R${:.2f}, mas com o desconto ele sai por R${:.2f}'.format(nomeProd, valorProd, descontoProd))
