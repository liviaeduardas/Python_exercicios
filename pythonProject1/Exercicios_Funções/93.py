# Programa que tenha uma função chamada ficha(), que receba dois parâmetros
# opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome='<Desconhecido>', gols=0):
    return f'O jogador {nome} fez {gols} gols no campeonato.'


jogador = str(input('Nome: '))
gol = str(input('Gols: '))

if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0

if jogador.strip() == '':
    print(ficha(gols=gol))
else:
    print(ficha(jogador, gol))

