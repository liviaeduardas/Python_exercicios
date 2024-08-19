# 10 termos de uma PA

print('='*20)
print('10 TERMOS DE UMA PA')
p = int(input('Informe o primeiro termo: '))
r = int(input('Razão: '))
décimo = p + (10 - 1) * r
for i in range(p, décimo, r):
    print(' {} '.format(i), end='->')
print('FIM')
