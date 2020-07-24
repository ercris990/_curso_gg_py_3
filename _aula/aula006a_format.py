# função print com o comando format
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
soma = n1 + n2
#print('A soma entre', n1, 'e', n2, 'é', soma)
print('A soma entre {} e {} vale {}'.format(n1, n2, soma))
