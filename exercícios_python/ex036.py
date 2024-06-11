casa = float(input('Qual o valor da casa? R$'))#Valor Casa
salario = float(input('Qual o seu salário? R$'))#Salário do comprador
pagar = int(input('Em quantos anos você vai financiar? R$'))#Quantos anos ele vai pagar.

prestacao = casa / (pagar*12)

print('Para pagar uma casa de R${:.2f} em {} anos. \nA prestação mensal será de R${:.2f}'.format(casa, pagar, prestacao))

if prestacao <= salario*30/100:
    print('O seu empréstimo foi LIBERADO!')
else:
    print('O seu empréstimo foi NEGADO.')
