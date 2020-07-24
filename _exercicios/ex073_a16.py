equipas = ('Corinthians', 'Palmeiras', 'Santos', 'Grémio', 'Cruzeiro',
           'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo',
           'Atlético-PR', 'Baia', 'São Paulo', 'Fluminense', 'Sport Recife',
           'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
cont = 0
print('{:=^150}'.format(' CLASSIFICAÇÃO BRASILEIRÃO '))
for position, t in enumerate(equipas):
    print(f'{position + 1}º. {t}')
print('{:=^150}'.format(' [ 5 ] PRIMEIROS - CAPEONATO BRASILEIRO '))
print(f'Os 5 primeiros classifcados são: {equipas[:5]}')
print('{:=^150}'.format(' [ 4 ] ULTIMOS CLASSIFICADOS '))
print(f'Os últimos 4 classificados são: {equipas[-4:]}')
print('{:=^150}'.format(' EQUIPAS ORGANIZADAS POR ORDEM ALFABÉTICA '))
print(f'Lista de times por ordem alfabetica: {sorted(equipas)}')
print('{:=^150}'.format(' CLASSIFICAÇÃO DA CHAPECOENSE '))
print(f'O Chapeconse esta na {equipas.index("Chapecoense")+1}ª posição.')
print('{:=^150}'.format(' FIM DO PROGRAMA '))
t
