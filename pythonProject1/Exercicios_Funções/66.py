# programa que tenha uma função chamada contador(), que receba três parâmetros:
# início, fim e passo. Seu programa tem que realizar três contagens
# através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep

def contador(i, f, p):
    print('-' * 40)
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i > f:
        c = i
        while c >= f:
            print(c, end=' ')
            c -= p
            sleep(0.5)
        print('FIM!')
    else:
        c = i
        while c <= f:
            print(c, end=' ')
            c += p
            sleep(0.5)
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)

print('-' * 40)
print('SUA VEZ:')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
pulo = int(input('Pulo: '))
contador(inicio, fim, pulo)


