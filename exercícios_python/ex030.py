numero = int(input('Digite um número para saber se ele é PAR ou IMPAR. '))

par = numero % 2

if par == 0:
    print('Esse número é PAR.')
else:
    print('Esse número é IMPAR.')
