nome = str(input('Qual é o seu nome: ')).strip()
if 'Ermano' in nome:
    print('Que nome lindo voce tem!')
else:
    print('Seu nome e tão normal!')
print('Bom dia, {}!'.format(nome))
