# Tuplas -> pessoas = ()
# Listas -> pessoas = []
# Dicionarios -> pessoas = {}
#
# ================================================
# Keys() -> Dados da memória
# Values() -> Identificador EX:('nome', 'sexo')
# Items() -> Trás os dois. keys e values.
# ================================================

# ======================================================
# Printando o dicionario
pessoas = {'nome': 'Gabriel', 'sexo': 'M', 'idade': 19}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')

# ======================================================
# Printando as keys()
print('-=' * 30)
print(f'{pessoas.keys()}')

# ======================================================
# Printando os values()
print('-=' * 30)
print(f'{pessoas.values()}')

# ======================================================
# Printando os items()
print('-=' * 30)
print(f'{pessoas.items()}')

# ======================================================
# Acessar keys, values e items por laços
# Esse exemplo trás apenas os campos da memória
print('-=' * 30)
for k in pessoas.keys():
    print(k)

# ======================================================
# Acessar keys, values e items por laços
# Esse exemplo trás apenas os valores da memória alocada. EX: nome = 'Gabriel'
print('-=' * 30)
for k in pessoas.values():
    print(k)

# ======================================================
# Acessar keys, values e items por laços
# Para usar o items precisamos da keys e values. Trazendo o identificador
# e o valor alocado neles
print('-=' * 30)
for k, v in pessoas.items():
    print(f'{k} = {v}')

# ======================================================
# Excluindo o um identificador e seu valor do dicionario
print('-=' * 30)
del pessoas['sexo']
print(pessoas)

# ======================================================
# Trocando valores em um identificador no dicionario
print('-=' * 30)
pessoas['nome'] = 'Camila'
pessoas['peso'] = 98.5
print(pessoas)

# ======================================================
# Dicionario dentro de uma lista
print('=-=' * 30)
brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}   # lista 1 - alocamento 0 - 1
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}    # lista 2 - alocamento 0 e 1
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]['sigla'])

# ======================================================
# Dicionario dentro de uma lista
print('=-=' * 30)
estado = dict()  # Declaração de dicionario
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
print('-' * 20)
for e in brasil:
    for k, v in e.items():
        print(v, end=' ')
#        print(f'O campo {k} tem o valor {v}')
#    print(e)
