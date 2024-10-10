# mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.

from time import sleep
cores = (
    '\033[m', # 0 - sem cores
    '\033[0;30;41m', # 1 Vermelho
    '\033[0;30;42m', # 2 Verde
    '\033[0;30;43m', # 3 Amarelo
    '\033[0;30;44m', # 4 Azul
    '\033[0;30;45m', # 5 Roxo
    '\033[7;40m', # 6 Branco
)
def ajuda(comand):
    título(f'Acessando o manual: {comand}', 4)
    print(cores[6], end='')
    help(comand)
    print(cores[0], end='')
    sleep(2)


def título(msg, cor=0):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('-'*tam)
    print(f' {msg}')
    print('-' * tam)
    print(cores[0], end='')
    sleep(1)

comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 5)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO', 1)
