# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
cont = 0

while True:
    lista.append(int(input('Informe um número: ')))
    cont += 1
    resp = str(input('Deseja continuar? [N|S] ')).strip().upper()
    if resp not in 'SN':
        resp = str(input('Deseja continuar? [N|S] ')).strip().upper()
    if resp == 'N':
        break

print(f'Você digitou {cont} números')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O número 5 faz parte da lista')
else:
    print('O número 5 não faz parte da lista')
