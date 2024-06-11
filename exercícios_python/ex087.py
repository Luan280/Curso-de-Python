lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = total = maior = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        lista[linha][coluna] = int(input(f"Digite um valor para [{linha}, {coluna}]: "))
print("-=" * 30)

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"[{lista[linha][coluna]:^5}]", end=" ")
        if lista[linha][coluna] % 2 == 0:
            par += lista[linha][coluna]
    print()
print(f"A soma dos valores pares é {par}.")

for linha in range(0, 3):
    total += lista[linha][2]
print(f"A soma dos valores da terceira coluna é {total}.")

for coluna in range(0, 3):
    if coluna == 0:
        maior = lista[1][coluna]
    elif lista[1][coluna] > maior:
        maior = lista[1][coluna]
print(f"O maior valor da segunda linha é {maior}.")
