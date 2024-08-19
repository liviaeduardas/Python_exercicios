# calculadora

from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
acabar = False

while not acabar:
    print('\nQual opção você deseja:')
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    r = int(input('Qual a opção: '))

    if r < 5 and r >= 1:
        if r == 1:
            print('A soma é {}'.format(n1 + n2))
        elif r == 2:
            print('A multiplicação é {}'.format(n1 * n2))
        elif r == 3:
            if n1 > n2:
                print('{} é maior que {}'.format(n1, n2))
            elif n2 > n1:
                print('{} é maior que {}'.format(n2, n1))
            else:
                print('São iguais')
        elif r == 4:
            n1 = int(input('Qual o novo valor: '))
            n2 = int(input('Qual o novo valor: '))
            print('Novos valores rigistrados!!')
    elif r == 5:
        print('Fim do programa!')
        acabar = True
    else:
        print('Não existe essa opção')

    sleep(2)
