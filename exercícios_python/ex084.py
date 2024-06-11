galera = list()
dados = list()

maior = 0
menor = 99999
while True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))

    if dados[1] > maior:
        maior = dados[1]
    if dados[1] < menor:
        menor = dados[1]

    galera.append(dados[:])
    dados.clear()
    continuar = str(input("Quer continuar [S/N]:"))
    if continuar in "Nn":
        break
print(F"Ao todo, você cadastrou {len(galera)} pessoas.")

print(F"O maior peso foi de {maior}Kg. Peso de ", end="")
for v in galera:
    if v[1] == maior:
        print(F"[{v[0]}] ", end="")
print()

print(F"O menor valor foi de {menor}. Peso de ", end="")
for v in galera:
    if v[1] == menor:
        print(F"[{v[0]}] ", end="")
print()
