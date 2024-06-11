velocidade = float(input('Qual é a velocidade do carro em KM/H:'))

# Calculo da multa
multa = (velocidade - 80) * 7

if velocidade >= 80:
    print('MULTADO! Você excedeu a velocidade máxima de 80KM/h.')
    print('Você deve pagar uma multa de R${}.'.format(multa))
else:
    print('Você não excedeu o limite de velocidade.')
