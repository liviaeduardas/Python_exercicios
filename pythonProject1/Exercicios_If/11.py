# Desenvolva um programa que leia o comprimento de três retas e diga
# ao usuário se elas podem ou não formar um triângulo.

a = float(input('Informe o lado A: '))
b = float(input('Informe o lado B: '))
c = float(input('Informe o lado C: '))

if a+b > c and a+c > c and c+b > a:
    print('Os segmentos acima {}PODEM FORMAR{} um triângulo!'.format('\033[1;32m','\033[m'))
else:
    print('Os segmentos acima {}NÃO PODEM FORMAR{} um triângulo!'.format('\033[1;31m','\033[m'))

