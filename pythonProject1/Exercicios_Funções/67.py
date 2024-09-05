#  Programa que tenha uma função chamada maior(), que receba vários parâmetros
#  com valores inteiros. Seu programa tem que analisar todos os valores e
#  dizer qual deles é o maior.

from time import sleep

def maior(*n):
    m = c = 0
    for i in n:
        if c == 0:
            m = i
        else:
            if i > m:
                 m = i
        c += 1
    print('~' * 20)
    print('Analisando valores....')
    print(f'{n} contém {c} valores.')
    print(f'O maior deles é {m}')
    sleep(0.5)


maior(1, 2, 4)
maior( 9, 2, 6, 8)
maior(0, 10, 11, 67)
maior()