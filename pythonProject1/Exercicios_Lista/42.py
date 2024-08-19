# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as
# suas respectivas posições na lista.

valores = list()
maior = menor = 0
for i in range(0, 5):
    valores.append(int(input(f'Informe um valor na posição {i}: ')))
    if i == 0:
        maior = menor = valores[i]
    else:
        if valores[i] > maior:
            maior = valores[i]
        if valores[i] < menor:
            menor = valores[i]

print('=-'*20)
print(f'Você digitou os valores {valores}')

print(f'O maior número é {maior} e está na posição', end=' ')
for i, v in enumerate(valores):
    if v == maior:
        print(i, end=' ')
print(f'\nO maior número é {menor} e está na posição', end=' ')
for i, v in enumerate(valores):
    if v == menor:
        print(i, end=' ')
