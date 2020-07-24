nome = str(input('Digite o seu nome: ')).strip().capitalize()
lista = ['Ana', 'Cláudia', 'Jéssica', 'Juliana', 'Rosa']
if nome == 'Ermano':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo' or nome == 'João':
    print('Seu nome é tão popular em Angola.')
elif nome in lista:
    print('Belo nome feminino.')
else:
    print('Seu nome é tão normal.')
print('Tenha um bom dia, {}!'.format(nome))
