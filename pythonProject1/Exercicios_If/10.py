# maior e menor valores de 3 números

n = float(input('Primeiro valor'))
n1 = float(input('Segundo valor'))
n2 = float(input('Terceiro valor'))
maior = n
menor = n
if n1 > maior and n1 > n2:
    maior = n1
if n2 > maior and n2 > n1:
    maior = n2
if n1 < menor and n1 < n2:
    menor = n1
if n2 < menor and n2 < n1:
    menor = n2
print('MAIOR = {}'.format(maior))
print('MENOR = {}'.format(menor))

