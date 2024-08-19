# o usuário possa digitar sete valores numéricos e cadastre-os
# em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

impares = list()
pares = list()
todos = list()

for i in range(0, 7):
    n = int(input(f'Informe o {i+1} valor: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

pares.sort()
impares.sort()
todos.append(pares[:])
todos.append(impares[:])
print(f'Os números pares são {todos[0]}')
print(f'Os números ímpares são {todos[1]}')

# outra forma

numeros = [[], []]

for i in range(0, 7):
    nu = int(input(f'Informe o {i+1} valor: '))
    if nu % 2 == 0:
        numeros[0].append(nu)
    else:
        numeros[1].append(nu)
numeros[0].sort()
numeros[1].sort()
print(f'Os números pares são {numeros[0]}')
print(f'Os números ímpares são {numeros[1]}')