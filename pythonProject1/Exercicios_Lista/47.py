# programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses
# abertos e fechados na ordem correta.

expressão = str(input('Informe a expressão: '))
pilha = []

for simbolo in expressão:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        # se já existir um parenteses ele vai deletar o último pq são pares
        # assim vai eliminando os pares juntos
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
# se não existir nenhum aprenteses na lista é pq achou todos os pares
if len(pilha) == 0:
    print('Expressão correta!')
else:
    print('Expressão incorreta!')
