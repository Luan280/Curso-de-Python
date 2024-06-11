from datetime import date

atual = date.today().year
cont = 0
cont2 = 0

for c in range(1, 7 + 1):
    nasc = int(input("Em que ano a {}º pessoa nasceu?: ".format(c)))
    idade = atual - nasc
    if idade >= 21:
        cont += 1
    elif idade <= 21:
        cont2 += 1

print("\nAo todo tivemos {} pessoas maiores de idade".format(cont))
print("E tambem tivemos {} pessoa menores de idade".format(cont2))

