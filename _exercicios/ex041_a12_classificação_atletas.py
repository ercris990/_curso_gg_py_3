from datetime import date
ano_nascimento = int(input('Digite o ano de nascimento: '))
idade = date.today().year - ano_nascimento
print('=' * 35)
print('Ano de Nascimento: {}.'.format(ano_nascimento))
print('Idade do Atleta: {} anos.'.format(idade))
if 0 < idade <= 9:
    print('Categoria do Atleta: Mirim.')
elif 10 <= idade <= 14:
    print('Categoria do Atleta: Infantil.')
elif 15 <= idade <= 19:
    print('Categoria do Atleta: Junior.')
elif idade == 20:
    print('Categoria do Atleta: Senior.')
else:
    print('Categoria dop Atleta: Master.')
print('=' * 35)
