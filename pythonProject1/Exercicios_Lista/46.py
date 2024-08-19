# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares
# e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista = []
pares = []
impares = []

while True:
    lista.append(int(input('Informe um número: ')))
    resp = str(input('Quer continuar? [S|N] ')).upper().strip()[0]
    if resp not in 'SN':
        print('Opção não valida!')
        resp = str(input('Quer continuar? [S|N] ')).upper().strip()[0]
    if resp == 'N':
        break

for i in range(0, len(lista)):
    if lista[i] % 2 == 0:
        pares.append(lista[i])
    else:
        impares.append(lista[i])

print(f'Lidta completa: {lista}')
print(f'Lista números pares: {pares}')
print(f'Lista números ímpares: {impares}')
