# teste para ver se a palavra é palindromo

frase = str(input('Informe uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for i in range(len(junto)-1, -1, -1):
    inverso += junto[i]
print(inverso)
if inverso == junto:
    print('é palindromo')
else:
    print('não é palindromo')
