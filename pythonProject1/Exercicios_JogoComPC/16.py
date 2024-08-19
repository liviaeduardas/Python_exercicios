# Jokenpo

import random
from random import randint
from time import sleep

print('Suas opções')
print('[ 1 ] PEDRA')
print('[ 2 ] PAPEL')
print('[ 3 ] TESOURA')
resp = int(input('Qual a sua jogada? '))

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!')
sleep(0.5)
print('-='*10)

comp = random.randint(1,3)

if resp == 1 and comp == 2:
    print('Computador jogou PAPEL')
    print('Jogador jogou PEDRA')
    print('-='*10)
    print('JOGADOR PERDEU')
elif resp == 1 and comp == 3:
    print('Computador jogou TESOURA')
    print('Jogador jogou PEDRA')
    print('-=' * 10)
    print('JOGADOR GANHOU')
elif resp == 2 and comp == 1:
    print('Computador jogou PEDRA')
    print('Jogador jogou PAPEL')
    print('-='*10)
    print('JOGADOR GANHOU')
elif resp == 3 and comp == 1:
    print('Computador jogou PEDRA')
    print('Jogador jogou TESOURA')
    print('-='*10)
    print('JOGADOR PERDEU')
elif resp == 3 and comp == 2:
    print('Computador jogou PAPEL')
    print('Jogador jogou TESOURA')
    print('-='*10)
    print('JOGADOR GANHOU')
elif resp == 2 and comp == 3:
    print('Computador jogou TESOURA')
    print('Jogador jogou PAPEL')
    print('-='*10)
    print('JOGADOR PERDEU')
else:
    print('ESCOLHERAM IGUAIS')
