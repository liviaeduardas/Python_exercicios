# Cores

cores = {'limpa':'\033[m', 'azul':'\033[34m',
         'amarelo':'\033[33m',
         'preto&branco':'\033[7;40m'}
print('{} azul {}{} amarelo {}{} preto e branco {}'.format(cores['azul'], cores['limpa'], cores['amarelo'],cores['limpa'],cores['preto&branco'],cores['limpa']))
