#  Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
#  A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai
#  mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando numeros: ', end=' ')
    for i in range(0,5):
        lista.append(randint(0,10))
    for i in range(0,len(lista)):
        print(lista[i], end=' ')
        sleep(0.5)


def somaPar(lista):
    par = 0
    for i in lista:
       if i % 2 == 0:
           par += i
    print(f'A soma dos números pares é {par}')

sorteio = list()
sorteia(sorteio)
print()
somaPar(sorteio)


