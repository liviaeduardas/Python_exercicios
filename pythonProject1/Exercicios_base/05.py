#Ler uma frase e mostrar quantas vezes o 'A' aparece, a primeira e a ultima posição

frase = str(input('Digite uma frase: ')).strip().lower()
print('A letra A aparece {} vezes'.format(frase.count('a')))
print('A primeira letra A parece na posição {}'.format(frase.find('a')+1))
print('A ultima letra A aparece na posição {}'.format(frase.rfind('a')+1-frase.count(' ')))