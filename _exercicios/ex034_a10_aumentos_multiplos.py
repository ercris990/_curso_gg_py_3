salario = float(input('Digite o salário do colaborador: AOA '))
print('------------------------------------------')
if salario <= 1250.00:
    taxa = (salario * 15 / 100)
    novo = salario + taxa
else:
    taxa = (salario * 10 / 100)
    novo = salario + taxa
print('Salário Anterior: AOA {:.2f}'.format(salario))
print('Valor do Aumento: AOA {}'.format(taxa))
print('Salário Actual: AOA {:.2f}'.format(novo))
