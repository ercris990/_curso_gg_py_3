val_casa = float(input('Qual o valor da casa: '))
salario = float(input('Qua o seu salário: '))
prazo = int(input('Em quantos anos pretende pagar: '))
prest_mensal = val_casa / (prazo * 12)
taxa_esforco = (prest_mensal * 100) / salario
# ----------------------------------------------------------------------------------------------------------------------
print('=*=' * 13)
if taxa_esforco <= 30:
    print('O seu emprestimo foi APROVADO.')
    print('Prazo de Pagamento: {} anos / {} meses.'.format(prazo, prazo * 12))
    print('Prestão Mensal: AOA {:.2f}'.format(prest_mensal))
    print('Taxa de Esforço: {:.2f} %'.format(taxa_esforco))
else:
    print('O seu empréstimo foi NEGADO.')
    print('A taxa de esforço excede o valor permitido (30%)')
    print('Taxa de Esforço {:.2f} %'.format(taxa_esforco))
print('=*=' * 13)
# ----------------------------------------------------------------------------------------------------------------------
