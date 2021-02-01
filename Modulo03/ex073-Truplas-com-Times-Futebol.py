times = ('Bayern', 'Atlético Madrid', 'Lokomotiv', 'RB Salzburg', 'Shakhtar', 'Inter', 'Real Madrid',
         'Manchester City', 'Porto', 'Olympiacos', 'Olympique', 'Liverpool', 'Atalanta', 'Ajax',
         'Midtjylland', 'Chelsea', 'Barcelona', 'Juventos', 'PSG' 'Borussia Dortmund')

print('-='*15)
print(f'Lista de times: {times}')
print('-='*15)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-='*15)
print(f'Os 4 últimos times da Champions League é: {times[-4:]}')
print('-='*15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*15)
print(f'O Real Madrid está na {times.index("Real Madrid")+1}ª posição')
