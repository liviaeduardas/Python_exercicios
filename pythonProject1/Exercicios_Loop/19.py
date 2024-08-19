# teste para ver se o número é primo

n = int(input('Digite um número:'))
t = 0
for i in range(1, n + 1):
    if n % i == 0:
        print('\033[36m', end='')
        t += 1
    else:
        print('\033[35m', end='')
    print('{} '.format(i), end='')
print('\n{}O numero {} foi dividido {} vezes'.format('\033[m', n, t))
if t == 2:
    print('É PRIMO!!!!')
else:
    print('NÃO É PRIMO')
