#  leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
#  No final, mostre um boletim contendo a média de cada um e
#  permita que o usuário possa mostrar as notas de cada aluno individualmente.

lista = list()
informações = list()

while True:
    lista.append(str(input('Nome: ')))
    nota1 = int(input('Nota 1: '))
    lista.append(nota1)
    nota2 = int(input('Nota 2: '))
    lista.append(nota2)
    media = (nota1 + nota2)/2
    lista.append(media)
    informações.append(lista[:])
    lista.clear()
    resp = str(input('Continuar? [S|N] ')).strip().upper()[0]
    if resp not in 'NS':
        resp = str(input('Continuar? [S|N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-='*20)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')

for i in range(0, len(informações)):
    print(f'{i:<4}', end='')
    print(f'{informações[i][0]:<10}', end='')
    print(f'{informações[i][3]:>8}', end='')
    print()

while True:
    print('-=' * 20)
    indice = int(input('Mostrar as notas de qual aluno?(999 interrompe) '))
    if indice == 999:
        break
    else:
        print(f'Notas de {informações[indice][0]} são {informações[indice][1]} {informações[indice][2]}')
