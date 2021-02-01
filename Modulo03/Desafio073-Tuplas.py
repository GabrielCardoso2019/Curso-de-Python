times = ('Bayern', 'Atlético Madrid', 'Lokomotiv', 'RB Salzburg', 'Shakhtar', 'Inter', 'Real Madrid',
         'Manchester City', 'Porto', 'Olympiacos', 'Olympique', 'Liverpool', 'Atalanta', 'Ajax',
         'Midtjylland', 'Chelsea', 'Barcelona', 'Juventos', 'PSG' 'Borussia Dortmund')

print('-=-'*20)
print('\033[01;31mCLASSIFICAÇÃO DE TIMES DA CHAMPIONS LEAGUE\033[m')
print('-=-'*20)
print('')
print('==='*20)
print(f'Times da Champions League: {times}')
print('==='*20)
print(f'Os 5 primeiros colocados: {times[0:5]}')
print('==='*20)
print(f'Os últimos 4 colocados: {times[-4:]}')
print('==='*20)
print(f'Times na ordem alfabética: {sorted(times)}')
print('==='*20)
print(f'O time que era bom: {times[6]}')
