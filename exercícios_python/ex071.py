print("==" * 20)
print("             BANCO DO BRASIL")
print("==" * 20)

count = 0
valor = int(input("Qual valor você quer sacar: R$"))
total = valor
cedula = 100
totcedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totcedula += 1
    else:
        print(f"Total de {totcedula} cédulas de R${cedula}")
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totcedula = 0
        if total == 0:
            break
print("==" * 20)
print("Volte sempre ao BANCO DO BRASIL! Tenha um bom dia!")
