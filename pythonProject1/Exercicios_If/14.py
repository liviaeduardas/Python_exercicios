# leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar
# ou se já passou do tempo do alistamento.
#  mostrar o tempo que falta ou que passou do prazo.

nasc = int(input('Ano de nascimento: '))
id = 2024 - nasc
print('Quem nasce em {} tem {} anos em 2024!'.format(nasc, id))
if id == 18:
    print('Está na hora exata de se alsita no serviço militar')
elif id < 18:
    an = 18 - id
    print('Faltam {} anos para o alistamento'
          '\nSeu alistamento será em {}'.format(an, 2024 + an))
else:
    an = id - 18
    print('Já se passaram {} anos do seu alistamento'.format(an))
    print('Deveria ter se alistado em {}'.format(2024 - an))


