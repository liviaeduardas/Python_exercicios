# leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

total = i = menor = maisdemil = 0
maisbarato = ' '
while True:
    print('='*20)
    print('loja super baratão'.upper())
    print('=' * 20)
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    total += preço
    i += 1
    if i == 1:
        menor = preço
        maisbarato = nome
    else:
        if preço < menor:
            menor = preço
            maisbarato = nome
    if preço > 1000:
        maisdemil += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Desja continuar? [S|N]')).strip().upper()
    if resp == 'N':
        break
print(f'Total gasto: {total}')
print(f'Total de produtos que custão mais de mil: {maisdemil}')
print(f'Produto mais barato foi {maisbarato}')
