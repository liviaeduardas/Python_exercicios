# MOSTRA O PRIMEIRO E ULTIMO NOME

nome = str(input('Informe seu nome completo: ')).strip()
nome1 = nome.split()
print('Prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome1[0]))
print('Seu ultimo nome é {}'.format(nome1[len(nome1)-1]))
