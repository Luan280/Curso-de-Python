lista = [[], []]

for v in range(1, 8):
    valores = int(input(f"Digite o {v}° valor: "))
    if valores % 2 == 0:
        lista[0].append(valores)  # Valor par
    else:
        lista[1].append(valores)  # Valor ímpar
lista[0].sort()
lista[1].sort()

print(f"Os valores pares foram: {lista[0]}")
print(f"Os valores ìmpares fora: {lista[1]}")
