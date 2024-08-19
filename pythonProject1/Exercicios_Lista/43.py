# Crie um programa onde o usuário possa digitar vários valores
# numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro,
# ele não será adicionado. No final, serão exibidos todos os valores
# únicos digitados, em ordem crescente.

lista = list()

while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Adicionado com sucesso!')
    else:
        print('Este número já existe! Não vou adiciona-lo')
    resp = str(input('Deseja continuar? [S|N] ')).strip().upper()
    if resp == 'N':
        break
lista.sort()
print(f'Você escolheu os valores {lista}')
