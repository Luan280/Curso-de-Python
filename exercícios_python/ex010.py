reais = float(input(f"Quantos reais você tem na carteira? R$"))
dollar = reais/4.78
euro = reais/ 5.40
print("Com R${:.2f} você consegue comprar {:.2f} Dólares e {:.2f} Euros.".format(reais, dollar, euro))