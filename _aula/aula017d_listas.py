valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print('_' * 45)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v};')
print('_' * 45)
print(valores)
print('Cheguei ao FIM da lista.')
