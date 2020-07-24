valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
for v in valores:
    print(f'{v}...')
print('*' * 40)
for chave, valor in enumerate(valores):
    print(f'> Na posição {chave + 1} encontrei o valor {v};')
print('Cheguei ao FIM da lista.')
