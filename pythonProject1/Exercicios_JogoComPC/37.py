# Crie um programa que vai gerar cinco números aleatórios
# e colocar em uma tupla. Depois disso, mostre a listagem de
# números gerados e também indique o menor e o maior valor que estão na tupla.
import random
from random import randint
numeros = (random.randint(0,10), random.randint(0,10),
           random.randint(0,10), random.randint(0,10),
           random.randint(0,10))
cont = 1
for i in range(0, len(numeros)):
    if cont == 1:
        maior = numeros[i]
        menor = numeros[i]
    if numeros[i] > maior:
        maior = numeros[i]
    elif numeros[i] < menor:
        menor = numeros[i]
    cont += 1
print(f'Os numeros são {numeros}')
print(f'O maior é {maior} e o menor é {menor}')

# outra forma

for i in numeros:
    print(f'{i}', end=' ')
print(f'\nO maior valor é {max(numeros)}')
print(f'O menor valor é {min(numeros)}')

