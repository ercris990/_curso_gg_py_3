nome_cid = str(input('Digite o nome da cidade: ')).strip()
x = nome_cid.split()
print('O nome da cidade digitada é: {}'.format(nome_cid))
print('A cidade começa com SANTO: {}'.format('SANTO' in x[0].upper()))
print('\n------------ OPÇÃO II ------------')
print('O nome da cidade digitada é: {}'.format(nome_cid))
print('A cidade começa com SANTO: {}'.format(nome_cid[:5].upper() == 'SANTO'))
