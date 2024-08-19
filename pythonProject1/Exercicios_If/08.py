#Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

v = int(input('Informe a velocidade do carro: '))
if v > 80:
    m = float((v-80)*7)
    print('MULTADO! Você escedeu o limite permitido de 80 Km/h')
    print('Você deve pagar R${:.2f}'.format(m))
print('Tenha um bom dia! Dirija com seguranaça!')
