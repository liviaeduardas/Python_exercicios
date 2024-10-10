# programa que tenha uma função notas() que pode receber várias notas
# de alunos e vai retornar um dicionário com as seguintes informações:
#  – Quantidade de notas
#  – A maior nota
#  – A menor nota
#  – A média
#  – A situação (opcional)

def notas(*nota, situacao=False):
    """
    -> Função para calcular quantidade de notas, maior nota, menor nota,
     média e situação do aluno
    :param nota: Pega a quantidade de notas que o usuário quiser entrar
    :param situacao: Mostra ou não a situação do aluno
    :return: Dicionário com as informações do aluno, contendo ou não a situação
    """
    informações = dict()
    informações['Total'] = len(nota)
    informações['Maior'] = max(nota)
    informações['Menor'] = min(nota)
    informações['Média'] = sum(nota)/len(nota)
    if situacao:
        if informações['Média'] > 5:
            informações['Situação'] = 'ÓTIMO'
        elif informações['Média'] <= 5:
            informações['Situação'] = 'RUIM'
    return informações

resp = notas(10, 9.9, 9, situacao=True)
print(resp)
help(notas)


