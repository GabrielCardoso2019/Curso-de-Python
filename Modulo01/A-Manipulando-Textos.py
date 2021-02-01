frase = 'Curso em Vídeo Python'

# Mostra a 3º letra da frase
print(frase[3])

# Mostra a 3º letra até a 13º da frase
print(frase[3:13])

# Mostra da 13º até a final
print(frase[13:])

# Mostra da 3º letra até a 15º pulando em 3
print(frase[3:15:3])

# pula de 3 em 3 letras na frase
print(frase[::2])

# Texto longo de forma fácil
print("""Lorem Ipsum é simplesmente uma simulação de
         texto da indústria tipográfica e de impressos, e vem sendo
         utilizado desde o século XVI, quando um impressor desconhecido
         pegou uma bandeja de tipos e os embaralhou para fazer um livro de
         modelos de tipos. Lorem Ipsum sobreviveu não só a cinco séculos!""")

# Contar qnts vezes tem determinado caracter
print(frase.count('o'))

# Contar qnts vezes tem determinada letra com Uppercase
print(frase.upper().count('O'))

# Conta quantas letras tem. Add com os espaços
print(len(frase))

# Conta quantas letras tem. Remove com os espaços
print(len(frase.strip()))

# Troca uma palavra pela outra
print(frase.replace('Python', 'Android'))

# verifica se a palavra está na frase
print('Curso' in frase)

# posição da palavra
print(frase.find('Curso'))

# busca a frase em minusculo
print(frase.lower().find('vídeo'))

# Divisão das palavras - lista
"""print(frase.split())"""
divindo = frase.split()
print(divindo[0])  # <- mostra apenas o 1º item da lista
print(divindo[2][3])  # <- mostra a 2º palavra da frase e a 3º letra dessa palavra
