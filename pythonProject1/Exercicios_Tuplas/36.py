#  Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
#  Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = ('Flamengo', 'Botafogo', 'Palmeiras', 'Fortaleza', 'Cruzeiro',
         'São Paulo', 'Bahia', 'Athletico-PR', 'Atlético-MG', 'Bragantino',
         'Vasco', 'Criciúma', 'Juventude', 'Internacional', 'Corinthians',
         'Grêmio', 'Vitória', 'Cuiabá', 'Fluminense', 'Atlético-GO')
print('='*20)
print('{:^20}'.format('TIMES BRASILEIRÃO'))
print('='*20)
print(f'Os times são: {times}')
print(f'Os 5 primeiros são: {times[:5]}')
print(f'Os ultimos quatro colocados são: {times[-4:]}')
print(f'Ordem alfabética {sorted(times)}')
print(f'O time do cruzeiro esta em {times.index("Cruzeiro")+1} lugar')
