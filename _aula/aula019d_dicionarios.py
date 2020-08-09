pessoas = {'Nome': 'Ermano Crostovao', 'Genero': 'M', 'Idade': 30}
pessoas['Peso'] = 177.00    # Adiciona um elemento no dicionario
# del pessoas['Genero']     # Elimina o elemento do dicionario
pessoas['Nome'] = 'Leandro'
for k, v in pessoas.items():
    print(f'{k} = {v}')
