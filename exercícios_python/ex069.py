print("-" * 30)
print("     CADASTRE UMA PESSOA   ")
print("-" * 30)
count= countH = countM = homens = mulheres = 0

while True:
    idade = int(input("Idade: "))
    if idade > 18:
        count += 1
    while True:
        sexo = str(input("Sexo: [M/F] ")).upper()
        if sexo == "M":
            countH += 1
        elif sexo == "F" and idade < 18:
            countM += 1
        if sexo in "MF":
            break
    print("-" * 30)
    continuar = str(input("Quer continuar? [S/N]")).upper()
    print("-" * 30)

    if continuar in "N":
        break
print(f"Total de pessoas com mais de 18 anos: {count}.")
print(f"Ao todo temos {countH} homens cadastrados.")
print(f"E temos {countM} mulheres com menos de 20 anos.")
