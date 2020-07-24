totalpessoas = totalpessoas18 = totalhomens = totalmulher20 = 0
while True:
    print('{:=^60}'.format(' CADASTRO UMA PESSOAS '))
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    print('_' * 26)
    opc = ' '
    while opc not in 'SN':
        opc = str(input('Desja continuar? [S//N] ')).strip().upper()[0]
    # -----------------------------------------------------------------
    totalpessoas += 1
    if idade >= 18:
        totalpessoas18 += 1
    if sexo == 'M':
        totalhomens += 1
    if sexo == 'F' and idade < 20:
        totalmulher20 += 1
    # -----------------------------------------------------------------
    if opc != 'S':
        break
print('{:"^60}'.format(' RELATORIO '))
print(f'Total de pessoas cadastradas: {totalpessoas}')
print(f'Pessoas maiores de 18 anos: {totalpessoas18}')
print(f'Total de homens cadastrados: {totalhomens}')
print(f'Total de mulheres menores de 20 anos: {totalmulher20}')
print('"' * 60 )
