# tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavra = ('LIVIA', 'EDUARDA', 'SILVEIRA', 'CURSO',
           'PYTHON', 'PROGRAMADOR')

for i in palavra:
    print(f'\nNa palavra {i} temos ', end='')
    for letra in i:
        if letra in 'AEIOU':
            print(letra, end='')