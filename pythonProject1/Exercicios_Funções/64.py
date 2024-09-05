# programa que tenha uma função chamada área(), que receba as dimensões
# de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def terreno(l, c):
    area = l * c
    print(f'A área do terreno {l}x{c} é de {area}m')


print('CONTROLE DE TERRENO')
terreno(l=float(input('Largura (m):')), c=float(input('Comprimento (m)')))

