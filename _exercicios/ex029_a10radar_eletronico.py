vel = float(input('Digite a velocidade do veiculo: '))
print('-' * 45)
if vel > 80:
    print('Veiculo com a velocidade de {:.2f} Km/h.'.format(vel))
    print('Está a {:.2f} Km/h acima da velocidade permitida.\nVocê foi multado.'.format(vel - 80))
    print('Valor da multa: {:.2f} R$'.format((vel - 80) * 7))
print('Tenha um bom dia, dirija com segurança!')
