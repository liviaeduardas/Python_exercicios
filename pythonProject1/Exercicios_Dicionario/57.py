#  leia nome e média de um aluno, guardando também a situação em um dicionário.
#  No final, mostre o conteúdo da estrutura na tela.
# Aprovado = média maior que 7
# Reprovado = média menor que 5
# Recuperação = média entre 5 e 6,9

dados = dict()

dados['Nome'] = str(input('Nome: '))
dados['Média'] = float(input('Média: '))

print('=-'*10)

if dados['Média'] >= 7:
    dados['Situação'] = 'APROVADO'
elif dados['Média'] <= 5:
    dados['Situação'] = 'REPROVADO'
else:
    dados['Situação'] = 'RECUPERAÇÃO'

for k, v in dados.items():
    print(f'- {k} é {v}')

