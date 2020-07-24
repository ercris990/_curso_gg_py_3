#Cadeia de Caracteres   #analise de string
frase = 'Curso em Video Python'
print(frase)
print('----------------------------------------')
print('O numero de caracteres da frase e de: {}'.format(len(frase)))    #conta o numero de caracteres da string (incluindo os espacos)
print(frase.count('o'))                                                 #conta quantas vezes existe a letra '0'
print(frase.count('o',0,13))                                            #conta quantas vezes 'o' aparece da posicao 0 ate 12
print(frase.find('deo'))                                                #indica a posicao de inicio da string entre aspas
print('Curso' in frase)                                                 #analisa se a string entre aspas existe na string contida na variavel (Retorna True/False)
print('----------------------------------------')
