sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe o seu sexo: [M/F] ')).upper().strip()
# ---------------------------------------------------------------------------------------------
if sexo == 'M':
    sexo = 'masculino'
else:
    sexo = 'feminino'
print('=+=' * 18)
print('> Sexo {} registrado com SUCESSO!.'.format(sexo.capitalize()))
