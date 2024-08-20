# programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que
# o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

sorteio = dict()
ranking = list()

for i in range(0, 4):
    sorteio[f'jogador{i+1}'] = randint(0,6)
    print(f'Jogador{i+1} tirou {sorteio[f"jogador{i+1}"]} no dado')
    sleep(1)

ranking = sorted(sorteio.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'{i+1} lugar {v[0]} com {v[1]}')


