print("-" * 35)
print("        LOJA SUPER BARATÃO     ")

count = countp = 0
menor = 99999

while True:
    print("-=" * 20)
    produto = str(input("Nome do produto: "))
    preço = float(input("Preço: R$"))
    continuar = str(input("Quer continuar? [S/N]")).upper()
    count += preço

    if preço >= 1000:
        countp += 1

    if preço < menor:
        menor = preço
        menor2 = produto

    if continuar in "N":
        break
print("------------------- FIM DO PROGRAMA -------------------")
print(f"O total da compra foi R${count:.2f}")
print(f"Temos {countp} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {menor2} que custava R${menor}")
