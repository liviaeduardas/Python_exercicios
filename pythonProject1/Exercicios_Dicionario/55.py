# dicionário:

dados = {'Nome': 'Lívia', 'Idade': 19, 'Sexo': 'F' }
print(f'A {dados["Nome"]} tem {dados["Idade"]} anos')
print()

# Mostrand as chaves, valores e completa:
print(dados.keys())
print(dados.values())
print(dados.items())
print()

# Acessando informações com loop
for k, v in dados.items():
    print(f'{k} = {v}')
print()

# trocando e adicionando valores:
dados['Idade'] = 20
dados['Peso'] = 55.9
print(dados.items())

