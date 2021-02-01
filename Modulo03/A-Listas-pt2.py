# lista composta. Possui uma lista dentro de outra
teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)

# ===================================================================
print('===' * 20)
# ===================================================================

galera = list()
# [:] faz cópia da lista
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

# ===================================================================
print('===' * 20)
# ===================================================================

galera = [['João', 19], ['Ana', 33], ['Maria', 45]]
# 1º[] colchetes pega o número da lista
# 2º[] colchetes pega o número de dentro da lista
print(galera[2][0])

# ===================================================================
print('===' * 20)
# ===================================================================

for p in galera:
    # Se usar o p[0] traz somente os nomes e p[1] as idades
    print(p)
    print(f'A idade de {p[0]} é de {p[1]} anos de idade')

# ===================================================================
print('===' * 20)
# ===================================================================

party = list()
dado = list()

totmai = totmen = 0

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    party.append(dado[:])
    dado.clear()
print(party)

# ===================================================================
print('===' * 20)
# ===================================================================

for p in party:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores de idade e {totmen} menores de idade')
