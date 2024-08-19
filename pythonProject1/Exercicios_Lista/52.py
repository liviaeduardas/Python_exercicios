# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = maior = terceira = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Valor [{l}, {c}] '))

print('=-'*10)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end=' ')
        if matriz[l][c] % 2 == 0:
             pares += matriz[l][c]
        if c == 2:
            terceira += matriz[l][c]
        if l == 1:
            if c == 0:
                maior = matriz[l][c]
            elif matriz[l][c] > maior:
                maior = matriz[l][c]
    print()

print('=-'*10)

print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {terceira}')
print(f'O maior valor da segunda linha é {maior}')
