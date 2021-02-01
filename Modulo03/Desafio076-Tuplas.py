lojaCarros = ('Mercedez C300 Sport', 250000,
              'Nissan GTR R35', 650000,
              'BMW M3 Coupe', 450000,
              'Land Rover Evoque', 520000,
              'Lamborghini Aventor', 1200000.00,
              'Porche 911 Carrera', 900000,
              'Porche Panamera', 850000,
              'Lamborghini Urus', 3500000.00,
              'Jaguar XER Sport', 750000,
              'Golf Turbo TSI', 150000,
              'Hylux SW4', 326000)

print('====' * 13)
print(f'{"LISTAGEM DE CARROS DE LUXO":^50}')
print('====' * 13)
for pos in range(0, len(lojaCarros)):
    if pos % 2 == 0:
        print(f'{lojaCarros[pos]:.<40}', end='')
    else:
        print(f'R${lojaCarros[pos]:>10.2f}')
print('====' * 13)
