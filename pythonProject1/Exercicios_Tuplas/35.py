# Crie um programa que tenha uma dupla totalmente preenchida com uma
# contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e
# mostrá-lo por extenso.

números = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatroze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    posição = int(input('Informe um numero de 0 a 20: '))
    if posição < 0 or posição > 21:
        posição = int(input('Informe um numero de 0 a 20: '))
    else:
        n = posição
        break

print(f'Você escolheu o numero {números[n]}')


