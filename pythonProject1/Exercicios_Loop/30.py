# leia a idade e o sexo de várias pessoas.
# O programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

maisdezoito = 0
homens = 0
menosvinte = 0

while True:
    print('-'*20)
    print('Cadastre uma pessoa'.upper())
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M|F]')).upper().strip()[0]
    print('-' * 20)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S|N]')).upper().strip()[0]
    if idade >= 18:
        maisdezoito += 1
    if sexo == 'F' and idade < 20:
        menosvinte += 1
    if sexo == 'M':
        homens += 1
    if resp == 'N':
        break
print('-'*20)
print(f'Pessoas com mais de 18 cadastradas: {maisdezoito}')
print(f'Homens cadastrados: {homens}')
print(f'Mulheres com menos de 20 anos cadastradas: {menosvinte}')
