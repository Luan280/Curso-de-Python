sexo = str(input("Escreva seu SEXO [M/F]")).strip().upper()[0]

while sexo not in "MmFf":
    sexo = str(input("Dados ínvalidos, Digite novamente:")).upper()
print("Acabou!")
