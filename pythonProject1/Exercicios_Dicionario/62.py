# Aprimore o exercício 60 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

dado = dict()
gol = list()
jogadores = list()
cont = 0

while True:
    dado['Nome'] = str(input('Nome do jogador: '))
    part = int(input(f'Quantas partidas {dado["Nome"]} jogou? '))

    for i in range(0, part):
        n = int(input(f'Quantos gols na partida {i + 1}: '))
        gol.append(n)
        cont += n
        dado['Gols'] = gol[:]
        dado['Total'] = cont

    jogadores.append(dado.copy())
    gol = ()
    while True:
        resp = str(input('Deseja adicionar mais jogadores? [S|N]')).strip().upper()[0]
        if resp in 'SN':
            break

    if resp == 'N':
        break

print('=-'*30)
print('Código', end=' ')
for i in dado.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('=-'*30)

while True:
    cod = int(input('Desea ver os dados de qual jogador: [999 para sair]'))
    if cod == 999:
        break
    if cod >= len(jogadores):
        print('ERRO!!!')
    else:
         for i, g in enumerate(jogadores[cod]['Gols']):
           print(f' - Na partida {i+1}, fez {g} gols')


