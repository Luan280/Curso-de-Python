print('>' * 20, 'LOJAS LIMA', '<' * 20)

valor = int(input('Preço das compras: R$'))

print('''FORMAS DE PAGAMENTO:
[ 1 ] á vista dinheiro/Débito
[ 2 ] á vista no cartão de crédito
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

pagamento = int(input('Qual é a opção de pagamento?'))

if pagamento == 1:
    dinheiro = valor-(valor*10/100)
    print('DINHEIRO/DÉBITO: Sua compra de R${:.2f} vai custar R$ {:.2f} no final. '.format(valor, dinheiro))

elif pagamento == 2:
    credito = valor-(valor*5/100)
    print('Á vista no CARTÃO DE CRÉDITO:Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(valor, credito))

elif pagamento == 3:
    print('Em até 2x no CARTÃO:Sua compra vai custar R${:.2f} '.format(valor))

elif pagamento == 4:
    parcelas = int(input('Quantas parcelas? '))
    juros = valor + (valor*20/100)
    print('Sua compra sera parcelada em {}x de R${:.2f} COM JUROS.'.format(parcelas, juros / parcelas))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(valor, juros))


