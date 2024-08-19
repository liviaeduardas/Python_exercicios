# tupla única com nomes de produtos e seus respectivos preços,
# na sequência. No final, mostre uma listagem de preços,
# organizando os dados em forma tabular.

listagem = ('lapís', 1.75,
            'borracha', 2,
            'caderno', 15.90,
            'estojo', 4.28,
            'compasso', 9.99,
            'mochila', 112.58,
            'livro',25.99)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for item in range(0, len(listagem)):
    if item % 2 == 0:
        print(f'{listagem[item]:.<30}', end='')
    else:
        print(f'R${listagem[item]:>7.2f}')
print('-'*40)