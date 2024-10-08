# Exercício impar par

def par(num=0):
    if num % 2 == 0:
        return True
    else:
        return False


n = int(input('Informe um valor: '))
if par(n):
    print('NÚMERO PAR!')
else:
    print('NÚMERO IMPAR!')
