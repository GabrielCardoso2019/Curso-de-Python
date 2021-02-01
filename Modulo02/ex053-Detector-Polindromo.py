# Strip() <- tira a frase
# Split() <- divide as palavras nos espaços
# .join() <- junta todas as palavras tirando espaços

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)

# Variável para colocar a frase em inverso
inverso = ''

# forma mais rapida. Começar no inicio (::) só que de trás para frente (-1)
inverso = junto[:: - 1]

# Uma forma de fazer
'''for letra in range(len(junto) + -1, -1, -1):
    inverso += junto[letra]'''

print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
