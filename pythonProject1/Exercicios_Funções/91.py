# Programa que tenha uma função chamada voto() que vai receber como parâmetro
# o ano de nascimento de uma pessoa, retornando um valor literal
# indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(ano):
    from datetime import date
    anoatual = date.today().year
    idade = anoatual - ano
    print(f'Com {idade} anos:', end=" ")
    if idade > 18:
        return 'VOTO OBRIGATÓRIO'
    elif idade < 16:
        return 'VOTO NEGADO'
    else:
        return 'VOTO OPCIONAL'


nascimento = int(input('Informe o ano em que você nasceu: '))
print(voto(nascimento))
