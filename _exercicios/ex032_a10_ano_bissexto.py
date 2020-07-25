from datetime import date
ano = int(input('Qual ano quer analisar? Digite 0 para analisar o ano actual: '))
if ano == 0:
    ano = date.today().year
print('---------------------------------------------------------------')
if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print('O ano de {} É BISSEXTO, ele tem 366 dias.'.format(ano))
else:
    print('O ano de {} NÃO É BISSEXTO, ele tem 365 dias.'.format(ano))
