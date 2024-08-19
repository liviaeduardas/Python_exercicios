#Programa que lê um número entre 0 e 1000 e mostre separado cada um

n = int(input('Digite um número: '))
uni = n // 1 % 10
dez = n // 10 % 10
cen = n // 100 % 10
mi = n // 1000 % 10
print('Analisando número {}'.format(n))
print('Unidade = {}'.format(uni))
print('Dezena = {}'.format(dez))
print('Centena = {}'.format(cen))
print('Milhar = {}'.format(mi))
