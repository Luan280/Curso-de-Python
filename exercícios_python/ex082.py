lista = []
lista_par = []
lista_impar = []

while True:
    num = int(input("Digite um valor: "))
    lista.append(num)
    continuar = str(input("Quer continuar? [S/N]")).upper()
    if continuar in "N":
        break

for v in range(0, len(lista)):
    if lista[v] % 2 == 0:
        lista_par.append(lista[v])
    elif lista[v] % 2 == 1:
        lista_impar.append(lista[v])

lista.sort()
print(f"A lista completa é {lista}.")
print(f"A lista de números pares é {lista_par}.")
print(f"A lista de números impares é {lista_impar}.")
