from datetime import date
ano_nascimento = int(input('Digite o seu ano de nascimento: '))
genero = str(input('Digite o gênero M/F: ')).upper()
ano_actual = date.today().year
idade = ano_actual - ano_nascimento
# ----------------------------------------------------------------------------------------------------------------------
print('=+=' * 17)
if genero == 'M':
    if idade < 18:
        print('Você nasceu em {} e tem {} anos de idade.'.format(ano_nascimento, idade))
        print('Faltam {} anos para se alistar ao serviço militar.'.format(18 - idade))
        print('O seu alistamento será em {}'.format(ano_nascimento + 18))
    elif idade == 18:
        print('Você nasceu em {} e tem {} anos de idade.'.format(ano_nascimento, idade))
        print('Chegou a hora de se alistar ao serviço militar.')
    else:
        print('Você nasceu em {} e tem {} de idade.'.format(ano_nascimento, idade))
        print('Passaram {} anos desde da sua data de alistamento.'.format(idade - 18))
        print('O seuano de alistameno foi em {}'.format(ano_nascimento + 18))
elif genero == 'F':
    print('O alistamento é apenas para que é do sexo masculino.')
else:
    print('Digite m para masculino e f para feminino ')
print('=+=' * 17)
# ----------------------------------------------------------------------------------------------------------------------
