medida = float(input('Uma distância em metrôs: '))
cm = medida * 100
mm = medida * 1000
km = medida / 1000

print('A medida de {}m corresponde a {:.0f}cm, {:.0f}mm, {:.1f}Km'.format(medida, cm, mm, km))
