# Jogo imper par com o computador

import random
from random import randint
c = 0
while True:
    comp = random.randint(1, 10)
    jogador = int(input('Informe um valor: '))
    ip = str(input('Par ou Ímpar? [P|I] ')).strip().upper()[0]
    soma = comp + jogador
    if soma % 2 == 0:
        rep = 'P'
    else:
        rep = 'I'
    if ip == rep:
        print(f'Jogador ganhou soma foi {soma} e computador escolheu {comp}')
        c += 1
    else:
        print(f'GAME OVER! Você venceu {c} vez')
        break
