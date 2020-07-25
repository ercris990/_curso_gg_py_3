from datetime import date
ano_actual = date.today().year
maior = 0
menor = 0
for i in range(1, 8):
    ano_nascimento = int(input('Em que ano a {}ª pessoa nasceu: '.format(i)))
    idade = ano_actual - ano_nascimento
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('Número de pessoas maiores de idade: {}'.format(maior))
print('Número de pessoas menores de idade: {}'.format(menor))
