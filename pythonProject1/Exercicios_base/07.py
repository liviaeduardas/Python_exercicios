#Programa que escolhe um número entre 0 e 5 e o
# usúário tenta descobrir

import random
from time import sleep
print('Vou pensar em um número entre 0 e 5. Tente adivinhar:')
n = int(input('Qual número eu pensei?'))
print('PROCESSANDO....')
sleep(3)
n1 = random.randint(0,5)
if n == n1:
    print('Você acertou!!!')
else:
    print('Você errou!! Pensei em {}'.format(n1))
