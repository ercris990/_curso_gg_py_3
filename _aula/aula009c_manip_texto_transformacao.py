#Cadeia de Caracteres   #transformacao de string
frase = 'Curso em Video Python'
print('String Original: {}'.format(frase))
print('----------------------------------------')
print(frase.replace('Python','Android'))                        #transforma a plavra Python em Android
print(frase.upper())                                            #transforma todos os caracteres minusculos em maiusculos
print(frase.lower())                                            #transforma todos os caracteres maiusculos em minusculos
print(frase.capitalize())                                       #transforma apenas o primeiro caractere em maiusculo
print(frase.title())                                            #transforma todas os caracteres iniciais em maiusculo
print('----------------------------------------')
frase1 = '   Aprenda Python  '
print('Segunda string: {}'.format(frase1))
print('----------------------------------------')
print(frase1.strip())                                           #remove os espacos em branco no princip[io e no final da string
print(frase1.rstrip())                                          #remove apenas os espacos em branco da direita
print(frase1.lstrip())                                          #remove apenas os espacos em branco da esquerda
print('----------------------------------------')
