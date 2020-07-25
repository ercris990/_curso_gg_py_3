teste = list()
teste.append('Ermano')
teste.append(30)
galera = list()
galera.append(teste[:])         # cria uma copia da lista teste
teste[0] = 'Shelcia'
teste[1] = 21
galera.append(teste[:])         # cria uma copia da lista teste
print(galera)
