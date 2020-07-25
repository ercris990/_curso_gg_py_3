dist_viagem = float(input('Qual a distancia da sua viagem: '))
print('--------------------------------------')
if 0 < dist_viagem <= 200:
    print('Distancia total da viagem: {:.2f} Km'.format(dist_viagem))
    print('Preço por Km: AOA 0.50')
    print('Preço da Passagem: AOA {:.2f}'.format(dist_viagem * 0.50))
else:
    print('Distancia dtotal da viagem: {:.2f} Km'.format(dist_viagem))
    print('Preço por Km: AOA 0.45')
    print('Preço da passagem: AOA {:.2f}'.format(dist_viagem * 0.45))
