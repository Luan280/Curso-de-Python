from random import randint

print("=-" * 15)
print("VAMOS JOGAR PAR OU ÍMPAR")
count = 0

while True:
    computador = randint(1, 10)

    print("=-" * 15)
    jogador = int(input("Diga um valor: "))
    jogador2 = str(input("PAR ou ÍMPAR? [P/I]")).upper()
    soma = computador + jogador

    if soma % 2 == 0:
        print("=-" * 15)
        print(f"Você escolheu {jogador} e o computador {computador}. total de {soma} que é PAR.")
    else:
        print("=-" * 15)
        print(f"Você escolheu {jogador} e o computador {computador}. total de {soma} que é IMPAR.")

    if soma % 2 == 0 and jogador2 == "P":
        print("Você VENCEU!!!")
        count += 1
    elif soma % 2 != 0 and jogador2 == "I":
        print("Você VENCEU!!!")
        count += 1
    else:
        print("Você PERDEU...")
        print(f"GAMER OVER! Você venceu {count} vezes.")
        print("=-" * 15)
        break
