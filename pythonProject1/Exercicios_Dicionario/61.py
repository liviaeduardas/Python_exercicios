# leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

dados = dict()
pessoas = list()
num = total_idade = 0
mulheres = list()
acima = list()

while True:
    dados['Nome'] = str(input('Nome: '))
    num += 1
    dados['Sexo'] = str(input('Sexo [M|F]: ')).strip().upper()[0]
    while True:
        if dados['Sexo'] not in 'MF':
            print('Resposta INVALIDA! Escolha entre [M|F]')
            dados['Sexo'] = str(input('Sexo [M|F]: ')).strip().upper()[0]
        else:
            break
    if dados['Sexo'] == 'F':
         mulheres.append(dados['Nome'])
    dados['Idade'] = int(input('Idade: '))
    total_idade += dados['Idade']
    pessoas.append(dados.copy())
    resp = str(input('Desja continuar? [S|N]')).strip().upper()[0]
    while True:
        if resp not in 'SN':
            print('Resposta INVALIDA! Escolha entre [S|N]')
            resp = str(input('Desja continuar? [S|N]')).strip().upper()[0]
        else:
            break
    if resp == 'N':
        break
print('-=' * 20)
print(f'A) Total de pessoas cadastradas é de {num}')
media = total_idade / num
print(f'B) A média de idades é {media}')
print(f'C) As mulheres cadastradas são {mulheres}')
print(f'D) Dados das pessoas que estão acima da média de idades')
for c in pessoas:
    if c['Idade'] > media:
        for k, i in c.items():
            print(f'{k} = {i}', end=' ')
