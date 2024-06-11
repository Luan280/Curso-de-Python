lista = []

while True:
    num = int(input("Digite um valor: "))
    if num not in lista:
        lista.append(num)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado! Não vou adicionar...")

    continua = str(input("Quer continuar? [S/N]")).upper()
    if continua in "N":
        print("=-" * 20)
        break
lista.sort()
print(f"Você digitou os valores {lista}")
