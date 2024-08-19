#  leia nome e peso de várias pessoas, guardando tudo em uma lista.
#  No final, mostre:
#  A) Quantas pessoas foram cadastradas.
#  B) Uma listagem com as pessoas mais pesadas.
#  C) Uma listagem com as pessoas mais leves.

pessoas = list()
dados = list()
maior = menor = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? [S|N] ')).upper().strip()
    if resp not in 'SN':
        resp = str(input('Quer continuar? [S|N] ')).upper().strip()
    if resp == 'N':
        break

print(f'Você cadastrou {len(pessoas)} pessoas')
print(f'O maior peso é {maior} de ', end='')
for i in pessoas:
    if i[1] == maior:
        print(i[0], end=' ')
print(f'\nO menor peso é {menor} de ', end='')
for i in pessoas:
    if i[1] == menor:
        print(i[0], end=' ')
