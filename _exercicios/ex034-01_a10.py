salario = float(input('Digite o salário do colaborador: AOA '))
print('--------------------------------------')
if salario > 1250.00:
    print('Salario sem Aumento: AOA {:.2f}'.format(salario))
    print('Valor do Aumento: AOA {:.2f} (10%)'.format(salario * 0.1))
    print('Salario com Aumento: AOA {:.2f}'.format(salario + (salario * 0.1)))
else:
    print('Salario sem Aumento: AOA {:.2f}'.format(salario))
    print('Valor do Aumento: AOA {:.2f} (15%)'.format(salario * 0.15))
    print('Salario com Aumento: AOA {:.2f}'.format(salario + (salario * 0.15)))
