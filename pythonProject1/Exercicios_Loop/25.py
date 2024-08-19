# PA com while e termina quando o usuário fala 0

primeiro = int(input('Informe o primeiro termo: '))
razão = int(input('Informe a razão: '))
termo = primeiro
i = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while i <= total:
        print('{} -> '.format(termo), end='')
        termo += razão
        i += 1
    print('PAUSA')
    mais = int(input('Quantos termos: '))
print('Fim')



