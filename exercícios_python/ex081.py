lista = []
while True:
    num = int(input("Digite um valor: "))
    if num < 0:
        print("Digite um valor maior que 0...")
    else:
        lista.append(num)
        continuar = str(input('Quer continuar? [S/N]:')).upper()
        if continuar in "N":
            break

    lista.sort(reverse=True)
print(f"Você digitou {len(lista)} elementos.")
print(f"Os valores em ordem decrescente são {lista}")

if 5 in lista:
    print(f"O valor 5 faz parte da lista e está na posição {lista.index(5)+1}.")
else:
    print("O valor 5 não faz parte da lista! ")
