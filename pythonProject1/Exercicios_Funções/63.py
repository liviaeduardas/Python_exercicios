# Funções exemplos

# declarando e executando funções com parametros
def soma(a, b):
    s = a + b
    print(s)


soma(b=4, a=5)
soma(23, 45)

# empacotamento
def contador(* núm):
    print(f'O numero é {núm}')


contador(2, 3, 4)
contador(6, 7, 1, 4, 9)

# Com for
def numeros(*num):
    for i in num:
        print(f'{i}')
    print('FIM')


numeros(2, 3, 4)
numeros(6, 7, 1, 4, 9)

# Funções com listas
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [5, 6, 7, 8]
dobra(valores)
print(valores)
