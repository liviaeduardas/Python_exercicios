# programa que tenha a função leiaInt(), que vai funcionar de forma
# semelhante ‘a função input() do Python, só que fazendo a validação
# para aceitar apenas um valor numérico.

def leiaInt(mensagem):
    """
    -> Funciona como o input
    :param mensagem: Recebe a pergunta para o usuário
    :return: A resposta do usuário transformada em int
    """
    ok = False
    valor = 0
    while True:
        n = str(input(mensagem))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Informe um valor válido!!!')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digital o número {n}')


