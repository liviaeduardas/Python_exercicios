#  ajude um jogador da MEGA SENA a criar palpites.
#  O programa vai perguntar quantos jogos serão gerados e vai
#  sortear 6 números entre 1 e 60 para cada jogo,
#  cadastrando tudo em uma lista composta.
import random
from random import randint
from time import sleep

jogo = list()

print('-'*30)
print('{:^30}'.format('JOGO MEGA SENA'))
print('-'*30)
nu = int(input('Quantos jogos você quer que eu sorteie? '))
print('{:^30}'.format('SORTEANDO OS JOGOS'))
sleep(1)

for j in range(0, nu):
    for n in range(0, 6):
        numeros = randint(1,60)
        if numeros not in jogo:
            jogo.append(numeros)
    jogo.sort()
    print(f'Jogo {j+1}: {jogo}')
    jogo.clear()
    sleep(1)




