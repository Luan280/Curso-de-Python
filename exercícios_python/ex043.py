peso = int(input('Qual o seu peso? (Kg): '))
altura = float(input('Qual a sua altura? (M): '))

imc = peso / (altura ** 2)

print('Massa corporal: {:.1f}'.format(imc))

if imc <= 18.5:
    print('Você está ABAIXO do peso!')

elif imc <= 25:
    print('Você está no peso IDEAL!')

elif imc <= 30:
    print('Você está ACIMA do peso ideal!')

elif imc <= 40:
    print('Você está OBESO!')

elif imc > 40:
    print('Você está na OBESIDADE MÓRBIDA!')
