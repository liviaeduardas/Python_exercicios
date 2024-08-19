#  Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#  No final do programa, mostre: a média de idade do grupo,
#  qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

id = 0
m = 0
hn = ''
hi = 0
for i in range(1, 5):
    print('\n----- PESSOA {} -----'.format(i))
    nome = str(input('NOME: '))
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO: ')).strip().lower()

    id += idade
    if sexo == 'feminino' and idade <= 20:
        m += 1
    if sexo == 'masculino' and idade > hi:
        hn = nome
        hi = idade
med = id / 4
print('Média de idades = {}'.format(med))
print('O sr.{} é o mais velho com {} anos'.format(hn, hi))
print('{} mulheres tem menos de 20 anos'.format(m))


