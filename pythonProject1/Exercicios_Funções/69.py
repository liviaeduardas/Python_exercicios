# Interactive Help
help(print)

print("-=" * 30)
# Doc
print(input.__doc__)

print("-=" * 30)
# Docstrings
# Vai mostrar as informções que você criou sobre a função
def contador(i, f, p):
    """
        -> Faz uma contagem e mostra na tela
        : i = Início
        : f = Fim
        : p = Passo
        : return = sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end=" ")
        c += p
    print('FIM!')

help(contador)

print("-=" * 30)
# Parâmetro opcional
# Quando uma função funciona mesmo se um paramentro estiver faltando
def somar( a=0, b=0, c=0):
    s = a + b + c
    print(f'SOMA = {s}')

print('Com todos os parametros:')
somar(5, 8,10)
print('Faltando 1 parametro:')
somar(5, 8)
print('Sem parametros: ')
somar()

