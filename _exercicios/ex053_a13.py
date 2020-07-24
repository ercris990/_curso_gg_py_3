frase = str(input('Digite uma frase: ')).strip().upper()    # strip: elimina os espacos antes e depois - #upper: transforma a frase em maiuscula
palavras = frase.split()                                    # split: separa a fase em uma lista/vetor
junto = ''.join(palavras)                                   # join: junta as palavras em uma unica string (removendo os espaços)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('\033[33mA frase [ {} ] É UM PALINDROMO!'.format(frase))
else:
    print('\033[31mA frase [ {} ] NÃO É UM PALINDROMO'.format(frase))
print('\033[mRESULTADO: {} <- -> {}'.format(junto, inverso))
