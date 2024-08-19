# listas com lista dentro
informações = list()
informações.append('Lívia')
informações.append(19)
pessoas = list()
pessoas.append(informações[:])
print(pessoas)

# mudando elemento e adicionando a lista
informações[0] = 'Spaik'
informações[1] = 9
pessoas.append(informações[:])
# vai mostrar a lista antiga e a nova pq já tinha feito a cópia da primeira
print(pessoas)

# estrutura composta
galera = [['João', 19], ['Maria', 20], ['Luísa',9]]
print(f'A {galera[2][0]} tem {galera[2][1]} anos')
print(galera[1])

# Imprimindo só um elemento de cada lista
for i in galera:
    print(f'{i[0]} tem {i[1]} anos de idade')

# Entrando indormações na lista
gente = list()
dado = list()
for i in range(0, 3):
    dado.append(str(input('NOME: ')))
    dado.append(int(input('IDADE: ')))
    # faz uma copia das informações da lista de dados formando uma nova lista
    gente.append(dado[:])
    # limpa a lista pro proximo loop ler dados novos
    dado.clear()
print(gente)
