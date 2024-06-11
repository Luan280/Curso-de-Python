a = int(input('Digite 3 números para saber qual é o maior: '))
b = int(input('Segundo: '))
c = int(input('terceiro: '))

#Verificando o maior número.
if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

#Verificando o menor número.
if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

print('O MENOR valor digitado foi {}.'.format(menor))
print('O MAIOR valor digitado foi {}.'.format(maior))