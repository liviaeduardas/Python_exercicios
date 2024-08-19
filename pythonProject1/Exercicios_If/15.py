#  considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

compra = float(input('Qual o valor das compras? R$'))

print('\nFORMAS DE PAGAMENTO:')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista no cartão')
print('[ 3 ] em até 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
r = int(input('Qual é a opção: '))

if r == 1:
    v = compra - (compra * 0.1)
    print('Sua compra recebeu 10% de desconto e vai custar R${}'.format(v))
elif r == 2:
    v = compra - (compra * 0.05)
    print('Sua compra recebeu 5% de desconto e vai custar R${}'.format(v))
elif r == 3:
    print('Não conseguimos desconto, valor a ser pago é R${}'.format(compra))
elif r == 4:
    p = int(input('Qual a quantidade de parcelas?'))
    comp = compra + (compra *0.2)
    par = comp / p
    print('As parcelas serão de R${:.2f} com JUROS'.format(par))
    print('Sua compra passará a custar R${:.2f}'.format(comp))
else:
    print('NÃO EXISTE ESSA OPÇÃO')
