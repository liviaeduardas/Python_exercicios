# Loop de números e média

n = int(input('Informe um número: '))
maior = menor = n
quant = 1
soma = n
resp = str(input('Deseja continuar [S|N]? ')).strip().upper()
while resp == 'S':
    n = int(input('Informe um número: '))
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    quant += 1
    soma += n
    resp = str(input('Deseja continuar [S|N]? ')).strip().upper()
media = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, media))
print('O maior é {} e o menor {}'.format(maior, menor))
