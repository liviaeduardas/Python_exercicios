# ESCOPO DE VARIÁVEIS
# variáveis globais e variáveis locais

def teste(b):
    b += 4
    c = 2
    print('Variáveis locais:')
    print(f'b + a = {b} c = {c}')

d = 5
teste(d)
print(f'Variavel global a = {d}')

print("-=" * 30)
def teste2(b):
    global a
    a = 8
    b += 4
    c = 2
    print('Variáveis locais:')
    print(f'a = {a} b + a(parametro) = {b} c = {c}')

a = 5
teste2(a)
print(f'Variavel global a = {a}')

print("-=" * 30)
# RETORNO DE VALORES
def somar(a=0, b=0):
    s = a + b
    return s
r1 = somar(2, 6)
r2 = somar(9,10)
print(f'Meus cálculos deram {r1} e {r2}')

