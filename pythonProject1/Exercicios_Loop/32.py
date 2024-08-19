# No início, pergunte ao usuário qual será o valor a ser sacado
# e o programa vai informar quantas cédulas de cada valor serão entregues.

print('-'*20)
print('{:^20}'.format('BANCO CENTRAL'))
quant = int(input('Informe o valor que deseja sacar: R$'))
total = quant
ced = 50
totalc = 0
while True:
    if total >= ced:
        total -= ced
        totalc += 1
    else:
        if totalc > 0:
            print(f'Total de {totalc} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalc = 0
        if total == 0:
            break
