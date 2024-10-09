# programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show,
# que será um valor lógico (opcional) indicando se será mostrado ou não
# na tela o processo de cálculo do fatorial.

def fatorial(numero, show=False):
    """
    -> Função que calcula fatorial
    :param numero: Numero que terá o fatorial
    :param show: Tem a opção de mostrar ou não a conta do fatorial
    :return: fatorial ou a conta com o fatorial
    -> Lívia Eduarda Silveira
    """
    f = 1
    if show:
        for c in range(numero, 0, -1):
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end="")
            else:
                print(' = ', end="")
    for c in range(numero, 0, -1):
        f *= c
    return f


print(f'Apenas o fatorial:', end=" ")
print(f'{fatorial(5, False)}')
print()
print(f'Fatorial e a conta:', end=" ")
print(f'{fatorial(5, True)}')
print()
print(f'Apenas o fatorial sem passar um parametro:', end=" ")
print(f'{fatorial(5)}')
