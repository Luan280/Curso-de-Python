resposta = "S"
count = maior = soma =0
menor = 999

while resposta != "N":
    numeros = int(input("Digite um número: "))
    resposta = str(input("Quer continuar? [S/N]:")).upper().strip()
    count += 1
    soma += numeros

    if numeros > maior:
        maior = numeros
    else:
        maior = maior

    if numeros < menor:
        menor = numeros
    else:
        menor = menor
media = soma / count
print(f"Você digitou {count} números e a média foi {media}")
print(f"O maior valor foi {maior} e o menor foi {menor}.")
