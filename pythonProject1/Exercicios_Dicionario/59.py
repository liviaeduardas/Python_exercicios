# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

dados = dict()

dados['Nome'] = str(input('Nome:')).strip()
dados['Idade'] = 2024 - int(input('Ano de nascimento: '))
dados['Carteira'] = int(input('Carteira de trabalho: (0 se não possui) '))
if dados['Carteira'] != 0:
    dados['Ano'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$'))

print('-' * 20)
print(f' - Nome: {dados["Nome"]}')
print(f' - Idade: {dados["Idade"]}')
if dados['Carteira'] != 0:
    print(f' - CTPS: {dados["Carteira"]}')
    print(f' - Ano de contratação:{dados["Ano"]}')
    print(f' - Salário: {dados["Salário"]}')
    apos = 2024 - dados['Ano']
    if apos >= 30:
        print(f'Você é aposentada com {apos} anos de contribuição')
    else:
        dados['Ano_ap'] = dados['Idade'] + (30 - apos)
        print(f'Você irá aposentar com {dados["Ano_ap"]} anos')
