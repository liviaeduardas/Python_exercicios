n = [0, 7, 9, 3]

# mudando um elemento
n[1] = 6

# adicionando um elemento
n.append(8)

# adicionando um número em determinada posição
n.insert(3, 4)

# colocando em ordem: crescente e decrescente
n.sort()
n.sort(reverse=True)

# removendo número: ultimo e selecionado
n.pop()
n.remove(3)

# outra forma de criar lista
lista = list()
lista.append(9)
lista.append(5)
lista.append(2)
for c, v in enumerate(lista):
    print(f'Na posição {c} encontrei o valor {v}')

# usuário entrando os valores da lista
numeros = list()
for i in range(0, 3):
    numeros.append(int(input('Digite um valor: ')))
print(numeros)

# copiando números de uma lista pra outra
a = [1, 4, 5, 6]
b = a[:]