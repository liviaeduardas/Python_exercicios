# programa que calcula o valor a se pagar de um aluguel de carro
# R$0,15 por km rodado e R$60,00 por dia

km = float(input('Qual a quantida de km percorridos? '))
dia = float(input('Qual a quantidade de dias? '))
v = (km * 0.15) + (dia * 60)
print('O valor a pagar é R${:.2f}'.format(v))