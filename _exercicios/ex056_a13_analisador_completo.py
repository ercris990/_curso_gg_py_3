soma_idade = 0
media_idade = 0
maioridadehomem = 0
nomemaisvelho = ''
cont_idade = 0
for p in range(1, 5):
    print('======== {}ª PESSOA ========'.format(p))
    nome = str(input('Nome: ')).capitalize().strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    # soma a idade de todas as pessoas
    soma_idade += idade
    # acha a idade e o nome do homem mais velho
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
    # conta o numero de mulheres com menos de 20 anos
    if idade < 20 and sexo in 'Ff':
        cont_idade += 1
# calcula a media de idades de todos
media_idade = soma_idade / p
print('=+=' * 20)
print('A média de idade do grupo é de {:.2f} anos de idade.'.format(media_idade))
print('O homem mais velho tem {} anos de idade e se chama {}.'.format(maioridadehomem, nomemaisvelho))
print('Ao todo tem {} mulher(es) abaixo dos 20 anos de idade.'.format(cont_idade))
