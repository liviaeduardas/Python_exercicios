# lista qem ordem assim que o usuário entra o valor

lista = []

for i in range(0, 5):
    n = int(input('Informe um número: '))
    # se for o primeiro número ou for maior que o último
    if i == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicicionado ao fim da lista')
    else:
        # começa a contrar as posições da lista
        pos = 0
        # enquanto a posição for menor que o fim da lista
        while pos < len(lista):
            # se o número for menor igual a lista na posição
            if n <= lista[pos]:
                # troca o numero na posição posição
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print('-=' * 10)
print(lista)
