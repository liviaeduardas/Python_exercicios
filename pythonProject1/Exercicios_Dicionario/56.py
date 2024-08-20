# adicionando dicionários dentro de listas:

estado1 = {'Uf': 'Minas Gerais', 'Sigla': 'MG'}
estado2 = {'Uf': 'São Paulo', 'Sigla': 'SP'}
brasil = list()
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print()

# Mostrando elemntos:
print(f'O estado de {brasil[0]["Uf"]} tem a sigla {brasil[0]["Sigla"]}')
print()

# usuários entrando as informações:
estado = dict()
pais = list()

for i in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    pais.append(estado.copy())
for e in pais:
    for k, v in e.items():
        print(f'O campo {k} é {v}')
print()
