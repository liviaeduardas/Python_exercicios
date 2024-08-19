# Desenvolva um programa que leia quatro valores pelo teclado e
# guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

n = (int(input('Informe um número: ')), int(input('Informe um número: ')),
    int(input('Informe um número: ')), int(input('Informe um número: ')))
print(f'O numero 9 apareceu {n.count(9)} vezes')
print(f'O primeiro 3 foi digitado na posição {n.index(3)+1}')
print('Os números pares são: ',end='')
for i in n:
    if i % 2 == 0:
        print(f'{i}', end=' ')

