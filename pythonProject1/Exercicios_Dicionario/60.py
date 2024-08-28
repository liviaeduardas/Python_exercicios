# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols.

dado = dict()
dado['Nome'] = str(input('Nome do jogador: '))
part = int(input(f'Quantas partidas {dado["Nome"]} jogou? '))
gol = list()
cont = 0

for i in range(0, part):
    n = int(input(f'Quantos gols na partida {i + 1}: '))
    gol.append(n)
    cont += n
dado['Gols'] = gol[:]
dado['Total'] = cont

print('=-'*30)
print(dado)

print('=-'*30)
for k, i in dado.items():
    print(f'O campo {k} tem o valor {i}')
print('=-'*30)

print(f'O jogador {dado["Nome"]} jogou {part} partidas.')
for i in range(0, len(gol)):
    print(f' - Na partida {i+1}, fez {gol[i]} gols')
print(f'Total de {dado["Total"]} gols.')
