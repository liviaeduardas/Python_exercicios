lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

# mais simples e em ordem alfabética:
for i in lanche:
    print(sorted(lanche))

# com len
for i in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[i]}')
print('Comi muito')

# mostrando o tamanho
for i in range(0, len(lanche)):
    print(i)

# sem usar len e mostrando a posição:
for c, i in enumerate(lanche):
    print(f'vou comer {i} na ordem {c}')
