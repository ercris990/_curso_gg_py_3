galera = list()
dados = list()
totmaior = totmenor = 0

print('=-=' * 20)
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    # cria uma copia da lista dados e coloca dentro da lista galera
    galera.append(dados[:])
    # elimina os dados a cada laço
    dados.clear()

print('=-=' * 20)
for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1

print('=-=' * 20)
if totmaior < 1:
    print(f'Não temos nenhum maior de idade.')
elif totmaior == 1:
    print(f'Temos apenas {totmaior} maior de idade.')
else:
    print(f'Temos {totmaior} maiores de idade.')

if totmenor < 1:
    print('Não temos nenhum menor de idade.')
elif totmenor == 1:
    print(f'Temo apenas {totmenor} menor de idade.')
else:
    print(f'Temos {totmenor} menores de idade.')
print('=-=' * 20)
