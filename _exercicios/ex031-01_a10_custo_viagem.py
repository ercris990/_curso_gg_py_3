distancia = float(input('Qual a distancia da sua viagem: '))
print('--' * 20)
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('Distância da Viagem: Km {}'.format(distancia))
print('Preço da Passagem: AOA {}'.format(preco))
