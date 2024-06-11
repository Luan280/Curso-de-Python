distancia = float(input('Qual a distância da viagem que você vai? Km:'))

# calculo das passagens
passagem = 0.50 * distancia
passagem2 = 0.45 * distancia

if distancia <= 200:
    print('A sua passagem custa R${:.2f}.'.format(passagem))
else:
    print('A sua passagem custa R${:.2f}'.format(passagem2))