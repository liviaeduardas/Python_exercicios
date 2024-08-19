# analisando nome

nome = str(input('Digire seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculo é {}'.format(nome.upper()))
print('Seu nome em minúsculo é {}'.format(nome.lower()))
print('Seu nome completo tem {} letras'.format(len(nome) - nome.count(' ')))
novo = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(novo[0], len(novo[0])))



